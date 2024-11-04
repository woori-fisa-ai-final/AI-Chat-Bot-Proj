from elasticsearch import Elasticsearch
import pandas as pd

# 1. Elasticsearch에서 특정 지표 데이터를 가져오는 함수
def fetch_data_from_elasticsearch(index_name='fred_data', fields=['FFTR', 'GDP Growth Rate', 'Unemployment Rate']):
    es = Elasticsearch('http://host.docker.internal:9200')
    query = {
        "query": {
            "match_all": {}
        }
    }
    
    result = es.search(index=index_name, body=query, size=10000)
    
    # Elasticsearch에서 가져온 결과를 DataFrame으로 변환
    hits = result['hits']['hits']
    data = [hit['_source'] for hit in hits]
    df = pd.DataFrame(data)
    
    # 필요한 지표만 선택
    df = df[['date'] + fields]
    df['date'] = pd.to_datetime(df['date'])
    return df


# 2. Plotly로 시각화
## FFTR, GDP Growth Rate, Unemployment Rate 지표를 시각화

import plotly.express as px

def visualize_data(df):
    df = df.sort_values('date')

    # FFTR 시각화
    fig_fftr = px.line(df, x='date', y='FFTR', title='Federal Funds Target Rate (FFTR) Over Time')
    fig_fftr.show()

    # GDP Growth Rate 시각화
    fig_gdp_growth = px.line(df, x='date', y='GDP Growth Rate', title='GDP Growth Rate Over Time')
    fig_gdp_growth.show()

    # Unemployment Rate 시각화
    fig_unemployment = px.line(df, x='date', y='Unemployment Rate', title='Unemployment Rate Over Time')
    fig_unemployment.show()


# 3. Django View 설정
## Django View에서 Elasticsearch에서 데이터를 가져와 시각화

from django.shortcuts import render
from .utils import fetch_data_from_elasticsearch

def plot_view(request):
    fields = ['FFTR', 'GDP Growth Rate', 'Unemployment Rate']
    df = fetch_data_from_elasticsearch(fields=fields)
    
    # 시각화 결과 저장
    plots = []
    
    # FFTR
    fig_fftr = px.line(df, x='date', y='FFTR', title='Federal Funds Target Rate (FFTR) Over Time')
    plots.append(fig_fftr.to_html(full_html=False))

    # GDP Growth Rate
    fig_gdp_growth = px.line(df, x='date', y='GDP Growth Rate', title='GDP Growth Rate Over Time')
    plots.append(fig_gdp_growth.to_html(full_html=False))

    # Unemployment Rate
    fig_unemployment = px.line(df, x='date', y='Unemployment Rate', title='Unemployment Rate Over Time')
    plots.append(fig_unemployment.to_html(full_html=False))

    return render(request, 'plot.html', {'plots': plots})

