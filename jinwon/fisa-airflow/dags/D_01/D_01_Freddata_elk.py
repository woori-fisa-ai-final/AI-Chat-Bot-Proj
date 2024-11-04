from datetime import datetime, timedelta
from email.policy import default
from textwrap import dedent


from datetime import datetime
from fredapi import Fred
import pandas as pd

import eland as ed

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


from elasticsearch import Elasticsearch, helpers



fred = Fred(api_key='5cafaa9a5f90981d7a9c005ea24ba83a')


# 현재 날짜를 end_date로 사용
end_date = datetime.today().strftime('%Y-%m-%d')

# 데이터 가져오기 함수
def fetch_data(series_id, start_date='2015-01-01', end_date=end_date):
    try:
        data = fred.get_series(series_id, observation_start=start_date, observation_end=end_date)
        return data
    except ValueError as e:
        print(f"Error fetching data for {series_id}: {e}")
        return None

def make_df() :

    # 주요 지표 데이터 조회
    fftr = fetch_data('DFEDTARU')
    gdp = fetch_data('GDP')
    gdp_growth_rate = fetch_data('A191RL1Q225SBEA')
    pce = fetch_data('PCE')
    core_pce = fetch_data('PCEPILFE')
    cpi = fetch_data('CPIAUCSL')
    core_cpi = fetch_data('CPILFESL')
    personal_income = fetch_data('PI')
    unemployment_rate = fetch_data('UNRATE')
    ism_manufacturing = fetch_data('MANEMP')
    durable_goods_orders = fetch_data('DGORDER')
    building_permits = fetch_data('PERMIT')
    retail_sales = fetch_data('RSAFS')
    consumer_sentiment = fetch_data('UMCSENT')
    nonfarm_payrolls = fetch_data('PAYEMS')
    jolts_hires = fetch_data('JTSHIL')

    # 데이터프레임으로 변환
    data_frames = {
        'FFTR': fftr,
        'GDP': gdp,
        'GDP Growth Rate': gdp_growth_rate,
        'PCE': pce,
        'Core PCE': core_pce,
        'CPI': cpi,
        'Core CPI': core_cpi,
        'Personal Income': personal_income,
        'Unemployment Rate': unemployment_rate,
        'ISM Manufacturing': ism_manufacturing,
        'Durable Goods Orders': durable_goods_orders,
        'Building Permits': building_permits,
        'Retail Sales': retail_sales,
        'Consumer Sentiment': consumer_sentiment,
        'Nonfarm Payrolls': nonfarm_payrolls,
        'JOLTS Hires': jolts_hires
    }

    # 데이터프레임 병합
    df = pd.DataFrame()
    for key, value in data_frames.items():
        if value is not None:
            temp_df = value.reset_index()
            temp_df.columns = ['date', key]
            if df.empty:
                df = temp_df
            else:
                df = pd.merge(df, temp_df, on='date', how='outer')
    
    return df


es = Elasticsearch('http://host.docker.internal:9200')

try :
    es.indice.create('fred_data')
except :
    pass

def dataframe_to_elasticsearch():
    df = make_df()
    ed.pandas_to_eland(
        pd_df=df,
        es_client=es,
        es_dest_index="fred_data",
        es_if_exists="append",
        es_refresh=True
        )

    

default_args = {
    'depends_on_past': False,
    'retires': 1,
    'retry_delay': timedelta(minutes=5)
}

# DAG 정의
with DAG(
    'fred_uploader_elasticsearch',
    default_args=default_args,
    description="연준 데이터를 Elasticsearch에 집어 넣습니다.",
    schedule_interval='@daily',
    start_date=datetime(2015, 1, 1),
    catchup=False,
    tags=['elasticsearch','test', 'fred']
) as dag:
    
    # PythonOperator 설정
    t1 = PythonOperator(
        task_id="upload_fred_data_to_elasticsearch",
        python_callable=dataframe_to_elasticsearch,
    )

    t1