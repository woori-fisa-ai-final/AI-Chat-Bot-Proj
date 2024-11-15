from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv
from opensearchpy import OpenSearch
import opensearch_py_ml as oml
import urllib3

# SSL 경고 무시
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# .env 파일 로드
load_dotenv()

# OpenSearch 설정
host = os.getenv("HOST")
port = os.getenv("PORT")
auth = (os.getenv("OPENSEARCH_ID"), os.getenv("OPENSEARCH_PASSWORD"))

# OpenSearch 클라이언트 설정
client = OpenSearch(
    hosts=[{'host': host, 'port': port}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=False
)

# API 설정
BASE_URL = "http://apis.data.go.kr/1130000/FftcBrandFrcsStatsService/getBrandFrcsStats"
API_KEY = os.getenv("FRANCHISE_KEY_DECODED")

def ensure_index_exists():
    """인덱스가 없을 경우에만 생성"""
    if not client.indices.exists(index='franchise_stats'):
        client.indices.create(
            index='franchise_stats',
            body={
                "settings": {
                    "index": {
                        "number_of_shards": 1,
                        "number_of_replicas": 1
                    }
                },
                "mappings": {
                    "properties": {
                        "yr": {"type": "keyword"},
                        "indutyLclasNm": {"type": "keyword"},
                        "indutyMlsfcNm": {"type": "keyword"},
                        "corpNm": {"type": "keyword"},
                        "brandNm": {"type": "keyword"},
                        "frcsCnt": {"type": "integer"},
                        "newFrcsRgsCnt": {"type": "integer"},
                        "ctrtEndCnt": {"type": "integer"},
                        "ctrtCncltnCnt": {"type": "integer"},
                        "nmChgCnt": {"type": "integer"},
                        "avrgSlsAmt": {"type": "float"},
                        "arUnitAvrgSlsAmt": {"type": "float"},
                        "date": {"type": "date"}
                    }
                }
            }
        )
        print("Index 'franchise_stats' created successfully.")

def fetch_franchise_data(year):
    """특정 연도의 데이터를 API에서 가져와 DataFrame으로 반환하는 함수"""
    def fetch_page(page_no):
        params = {
            'serviceKey': API_KEY,
            'pageNo': str(page_no),
            'numOfRows': '1000',
            'yr': str(year)
        }
        return requests.get(BASE_URL, params=params, verify=False)

    all_data = []
    first_response = fetch_page(1)
    root = ET.fromstring(first_response.content)

    # 총 데이터 수 확인
    total_count = int(root.find('.//totalCount').text)
    total_pages = (total_count + 999) // 1000  # 페이지 수 계산

    for page in range(1, total_pages + 1):
        response = fetch_page(page)
        page_root = ET.fromstring(response.content)

        for item in page_root.findall('.//item'):
            data_dict = {child.tag: int(child.text) if child.tag in ['frcsCnt', 'newFrcsRgsCnt', 'ctrtEndCnt', 'ctrtCncltnCnt', 'nmChgCnt'] 
                         else float(child.text) if child.tag in ['avrgSlsAmt', 'arUnitAvrgSlsAmt'] 
                         else child.text for child in item}
            data_dict['date'] = f"{year}-01-01"
            print(data_dict)
            data_dict['date'] = pd.to_datetime(data_dict['date'].apply(str) + '-01-01', errors='coerce')

            all_data.append(data_dict)

    return pd.DataFrame(all_data)

def concat_and_upload_data(**context):
    """신규 연도의 데이터를 가져와 기존 데이터와 concat하여 OpenSearch에 업로드하는 함수"""
    ensure_index_exists()

    # OpenSearch에서 기존 데이터 가져오기
    existing_data_query = {"query": {"match_all": {}}}
    existing_data = oml.opensearch_to_pandas(
        oml.DataFrame(client, 'franchise_stats')
    )

    # 새 연도 데이터 가져오기
    current_year = datetime.now().year - 1  # 전년도 데이터 가져오기
    new_data = fetch_franchise_data(current_year)
    if new_data.empty:
        print(f"No data available for year {current_year}.")
        return f"No data available for year {current_year}."

    # 데이터 합치기
    franchise_data_all = pd.concat([existing_data, new_data], ignore_index=True)

    # 날짜 형식 변환 (YYYY-MM-01)
    # data_dict['date'] = data_dict['date'].apply(str) + '-01'
    # data_dict['date'] = pd.to_datetime(data_dict['date'], errors='coerce')
    franchise_data_all['date'] = pd.to_datetime(franchise_data_all['date'].apply(str) + '-01')

    # 기존 데이터 삭제 후 새로운 데이터 업로드
    client.indices.delete(index='franchise_stats', ignore=[400, 404])  # 인덱스 삭제 후 다시 생성
    ensure_index_exists()
    
    oml.pandas_to_opensearch(
        pd_df=franchise_data_all,
        os_client=client,
        os_dest_index="franchise_stats",
        os_if_exists="append",
        os_refresh=True
    )
    print(f"Data for year {current_year} concatenated and uploaded successfully.")

# DAG 기본 설정
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG 정의
with DAG(
    'franchise_stats_etl_concat',
    default_args=default_args,
    description='신규 연도 데이터 수집 및 기존 데이터와 합쳐 OpenSearch에 업로드',
    schedule_interval='@yearly',
    catchup=False,
    tags=['opensearch', 'franchise', 'data']
) as dag:
    
    # 데이터를 새로 추가하고 기존 데이터와 concat하여 업로드
    upload_task = PythonOperator(
        task_id='concat_and_upload_data',
        python_callable=concat_and_upload_data,
    )