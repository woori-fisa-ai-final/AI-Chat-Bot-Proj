import urllib.request
from datetime import datetime, timedelta
import json
import pandas as pd
from konlpy.tag import Okt
from collections import Counter
from pytrends.request import TrendReq
import time
import os
import random
from opensearchpy import OpenSearch, helpers
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from dotenv import load_dotenv

load_dotenv()
# 환경 변수에서 OpenSearch 호스트와 인증 정보 불러오기
host = os.getenv("HOST")
port = os.getenv("PORT")
auth = (os.getenv("OPENSEARCH_ID"), os.getenv("OPENSEARCH_PASSWORD"))

client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = False
)

# Naver API 설정
client_id = os.getenv("NAVER_API_ID")
client_secret = os.getenv("NAVER_API_SECRET")

# 네이버 API 요청 함수
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.now(), url))
        return None

# 네이버 검색 API 데이터 수집
def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = f"/{node}.json"
    parameters = f"?query={urllib.parse.quote(srcText)}&start={start}&display={display}"
    url = base + node + parameters
    responseDecode = getRequestUrl(url)
    return json.loads(responseDecode) if responseDecode else None

# 네이버 뉴스 데이터 크롤링 및 전처리
def crawl_and_process_news():
    node = 'news'
    categories = ['경제', '스포츠', '사회', '정치']
    results = {}
    for category in categories:
        jsonResult = []
        start, display = 1, 100
        while True:
            jsonResponse = getNaverSearch(node, category, start, display)
            if jsonResponse is None or jsonResponse.get('display', 0) == 0:
                break
            jsonResult.extend(getPostData(post) for post in jsonResponse['items'])
            start += display
            if start > 1000:
                break
        results[category] = process_category_data(jsonResult, category)
    return results

def getPostData(post):
    title = post['title']
    description = post['description']
    link = post['link']
    pDate = datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    return {'title': title, 'description': description, 'link': link, 'pDate': pDate.strftime('%Y-%m-%d %H:%M:%S')}


# 텍스트 전처리 및 카테고리 데이터 처리
def preprocess_text(text, stop_words):
    okt = Okt()
    tokens = okt.nouns(text)
    return [word for word in tokens if len(word) > 1 and word not in stop_words]

def process_category_data(data, category):
    two_days_ago = datetime.now() - timedelta(days=2)
    df = pd.DataFrame(data)
    df['pDate'] = pd.to_datetime(df['pDate'])
    df_filtered = df[df['pDate'] > two_days_ago]
    stop_words = set(['것', '등', '및', '약', '또', '를', '을', '이', '가', '은', '는', category])
    df_filtered['processed_text'] = df_filtered['description'].apply(lambda x: preprocess_text(x, stop_words))
    all_words = [word for doc in df_filtered['processed_text'] for word in doc]
    word_counts = Counter(all_words)
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:15]
    return [{'word': word, 'count': count, 'links': [row['link'] for _, row in df_filtered.iterrows() if word in row['processed_text'][:3]]} for word, count in top_words]


# Google 트렌드 데이터 수집
def get_google_trends(keywords):
    pytrends = TrendReq(hl='ko-KR', tz=540)
    trends_data, trends_over_time = {}, {}
    for group in [keywords[i:i+5] for i in range(0, len(keywords), 5)]:
        for attempt in range(5):  # 최대 5번 시도
            try:
                pytrends.build_payload(group, timeframe='today 3-m')
                interest_over_time = pytrends.interest_over_time()
                for keyword in group:
                    trends_data[keyword] = interest_over_time[keyword].mean() if keyword in interest_over_time.columns else 0
                    trends_over_time[keyword] = interest_over_time[keyword].to_dict()
                break
            except Exception as e:
                print(f"Error: {str(e)}")
                wait_time = (2 ** attempt) + random.uniform(0, 1)  # 지수 백오프 + 무작위성
                time.sleep(wait_time)
        else:
            print(f"Failed to fetch data for group: {group}")
    return trends_data, trends_over_time

# 뉴스 데이터와 트렌드 데이터 결합
def combine_news_and_trends_df(news_data, trends_data, trends_over_time):
    combined_data = []
    for category, data in news_data.items():
        for item in data:
            combined_data.append({
                'word': item['word'],
                'count': item['count'],
                'trend_score': trends_data.get(item['word'], 0),
                'combined_score': item['count'] * (1 + trends_data.get(item['word'], 0) / 100),
                'links': item['links'],
                'trend_over_time': trends_over_time.get(item['word'], {}),
                'category': category
            })
    return pd.DataFrame(combined_data)

# 고정된 인덱스와 매핑 생성
def create_index_and_mapping():
    index_body = {
        "settings": {
            "index": {
                "knn": True
            }
        },
        "mappings": {
            "properties": {
                'date': {'type': 'date'},
                'word': {'type': 'keyword'},  # 단어를 고유 식별자로 사용
                'links': {'type': 'keyword'},  # 링크 배열
                'trend_score': {'type': 'float'},  # 초기 trend_score 칼럼
                'combined_score': {'type': 'float'},  # 초기 combined_score 칼럼
                'trend_over_time': {'type': 'object'},  # trend_over_time 필드
                "dynamic": "true"  # 새로운 칼럼을 자동으로 추가
            }
        }
    }

    if not client.indices.exists(index='trend_data'):
        client.indices.create(index='trend_data', body=index_body)
        print("새로운 인덱스 생성 완료")
    else:
        print("기존 인덱스가 존재합니다.")





## 데이터 적재를 위한 bulk_action 함수 생성
def create_bulk_actions_from_df(df, index_name):
    actions = []
    for _, row in df.iterrows():
        action = {
            "_index": index_name,
            "_source": row.to_dict()
        }
        actions.append(action)
    return actions

# OpenSearch에 결과 업로드 (고정 인덱스 사용)
def upload_to_opensearch(data):
    index_name = "trend_data"
    if not isinstance(data['combined_results'], dict):
        print("Error: combined_results is not a dictionary")
        return
    
    for category, items in data['combined_results'].items():
        if not isinstance(items, list):
            print(f"Error: items for category {category} is not a list")
            continue
        
        for item in items:
            if not isinstance(item, dict) or 'word' not in item:
                print(f"Error: Invalid item structure in category {category}")
                continue
            
            try:
                response = client.update(
                    index=index_name,
                    id=item['word'],
                    body={
                        "doc": {
                            f"trend_score_{datetime.now().strftime('%Y%m%d')}": item.get('trend_score', 0),
                            f"combined_score_{datetime.now().strftime('%Y%m%d')}": item.get('combined_score', 0),
                            f"trend_over_time_{datetime.now().strftime('%Y%m%d')}": item.get('trend_over_time', {}),
                            "links": item.get('links', [])
                        },
                        "doc_as_upsert": True
                    }
                )
                print(f"Document uploaded successfully: {item['word']}")
            except Exception as e:
                print(f"Failed to upload document: {item['word']}")
                print(f"Error: {str(e)}")


# 전체 파이프라인 실행 함수
def run_pipeline():
    news_data = crawl_and_process_news()
    trends_data, trends_over_time = get_google_trends([item['word'] for category in news_data.values() for item in category])
    combined_results = combine_news_and_trends_df(news_data, trends_data, trends_over_time)
    result = {'combined_results': combined_results}
    upload_to_opensearch(result)



# 파이프라인 실행
# run_pipeline()


# Airflow DAG 정의
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'trend_eunchai',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2015, 1, 1),
    catchup=False,
) as dag :
    t1 = PythonOperator(
        task_id='run_pipeline',
        python_callable=run_pipeline
    )
    
    t1 