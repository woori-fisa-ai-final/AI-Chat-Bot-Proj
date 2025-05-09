# 우대리(Woodarei)

🚧🚧 우리 FIS 아카데미 최종 프로젝트 🚧🚧

## 멤버
![image](https://github.com/user-attachments/assets/1d6c74fd-3abc-459d-b2ac-6b1513794758)

<table>
 <tr>
    <td align="center"><a href="https://github.com/awesome98"><img src="https://avatars.githubusercontent.com/awesome98" width="150px;" alt=""></td>
    <td align="center"><a href="https://github.com/eunchaipark"><img src="https://avatars.githubusercontent.com/eunchaipark" width="150px;" alt=""></td>
    <td align="center"><a href="https://github.com/euneun9"><img src="https://avatars.githubusercontent.com/euneun9" width="150px;" alt=""></td>
    <td align="center"><a href="https://github.com/JiyeonJeong02"><img src="https://avatars.githubusercontent.com/JiyeonJeong02" width="150px;" alt=""></td>
    <td align="center"><a href="https://github.com/yonggaljjw"><img src="https://avatars.githubusercontent.com/yonggaljjw" width="150px;" alt=""></td>
    <td align="center"><a href="https://github.com/SukbeomH"><img src="https://avatars.githubusercontent.com/SukbeomH" width="150px;" alt=""></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/awesome98"><b>👑 신호섭</b></td>
    <td align="center"><a href="https://github.com/eunchaipark"><b>박은채</b></td>
    <td align="center"><a href="https://github.com/euneun9"><b>이은지</b></td>
    <td align="center"><a href="https://github.com/JiyeonJeong02"><b>정지연</b></td>
    <td align="center"><a href="https://github.com/yonggaljjw"><b>조진원</b></td>
    <td align="center"><a href="https://github.com/SukbeomH"><b>홍석범</b></td>
  </tr>
</table>

## Manuals

### Git

- [git convention](./Documents/Manual/gitConvention.md)
- [git](./Documents/Manual/git.md)

## Project Structure

![image](https://github.com/user-attachments/assets/68344a40-8837-43da-bf9d-6a3ab9f0790a)

> [draw.io](https://app.diagrams.net/)를 이용하여 작성하였습니다.

- **Airflow**: 주기적으로 데이터를 수집하고, 전처리하는 역할을 합니다.
- **Elasticsearch**: 수집된 데이터를 저장하고, 백터화된 데이터를 저장, 검색하는 역할을 합니다.
- **Kibana**: Elasticsearch에 저장된 데이터를 시각화하는 역할을 합니다.
- **Django**: 사용자에게 데이터를 제공하고, 사용자의 요청에 따라 데이터를 Elasticsearch에서 가져와서 제공하는 역할을 합니다.
- **MySQL**: 사용자의 정보를 저장하고, Django에서 사용하는 데이터를 저장하는 역할을 합니다.

## Tech Stack

- Python 3.11
- Django 5.0
- MySQL 8.0
- Elasticsearch 7.15

---------

# 우대리
![image](https://github.com/user-attachments/assets/5062b5f9-07b0-44f5-8332-3aa8fc20830b)

## 프로젝트 소개
- 상품 개발 (및 마케팅)에 필요한 정보를 대시보드로 시각화 하며, 대시보드 내 정보를 챗봇을 통해 쉽게 이해하고 분석할 수 있도록 구현한 대직원 서비스

## 개발환경

- Front: HTML, CSS, JavaScript
- Back-end: 
  - Docker container
  - Port forwarding
  - Django
  - 제공된 API 활용
- 버전 및 이슈관리: 
  - GitHub
  - GitHub Issues
  - GitHub Project
- 협업 툴: 
  - Discord
  - Notion
  - GitHub Wiki
- 서비스 배포 환경: AWS


## 채택한 개발 기술과 브랜치 전략



## 기술 스택
- Python 3.12
- Django 5.0
- MySQL 8.0
- OpenSearch 2.18.0

## 프로젝트 구조
```
AI-Chat-Bot-Proj/
├── FISA/
│   ├── eunchai/
│   │   ├── watching_word.py
│   │   ├── another_script.py
│   │   └── ...
├── project/
│   ├── WEB/
│   │   ├── woodjango/
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   ├── asgi.py
│   │   │   ├── wsgi.py
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── static/
│   │   │   │   ├── css/
│   │   │   │   │   ├── style.css
│   │   │   │   └── js/
│   │   │   │       ├── script.js
│   │   │   ├── templates/
│   │   │   │   ├── index.html
│   │   │   │   └── dashboard/
│   │   │   │       ├── dashboard.html
│   │   │   └── migrations/
│   │   │       ├── __init__.py
│   │   ├── chatbot/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   └── urls.py
│   │   ├── manage.py
│   ├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

## 개발기간 및 작업관리

- 2024.10.25 ~ 2024.12.10

## 페이지별 기능
### 인증/인가 [초기화면]
- 서비스 접속 초기화면에서 회원가입 시 개인정보 조건 및 비밀번호 조건을 명시합니다.
  - 비밀번호 조건: 유사한 비밀번호, 글자수 제한 등
- 회원의 정보는 MySQL에 저장됩니다.

| 기능           | 설명               | GIF                           |
|----------------|--------------------|-------------------------------|
| 회원가입       | 개인정보와 조건 명시 | ![01 회원가입](https://github.com/user-attachments/assets/711e52c7-7062-4c42-aa40-d30d6efc3a61) |
| 로그인         | 로그인 화면        | ![02 로그인](https://github.com/user-attachments/assets/ff92dbbe-a304-45d9-bfd9-fee1b4b92f6d) |


### 대시보드 
(대시보드 1,2,3번이 용량 문제로 안올라감)

## 챗봇 기능

챗봇 아이콘을 클릭하면 챗봇 기능을 사용할 수 있습니다.  
아래는 주요 기능과 챗봇 실행 구조 및 화면 예시입니다.

---

### 📌 주요 기능
1. **질의 / 응답 기능**  
   데이터베이스로부터 데이터를 추출하여 참고 후 답변을 생성합니다.
2. **히스토리 기능**  
   모든 DB를 기반으로 대화 이력을 관리하고 저장합니다.
3. **멀티턴 기능**  
   연속적인 대화를 이해하고 맥락을 유지합니다.
4. **평가 기능**  
   사용자의 피드백을 수집해 챗봇 성능을 지속적으로 개선합니다.
5. **파워모드**  
   확장된 키워드 추출 및 웹 크롤링을 통해 심화 정보를 제공합니다.

---

### 🛠 챗봇 구성 구조
![챗봇그림](https://github.com/user-attachments/assets/f036e16a-9f2d-4d9c-90ca-15635c49405a)

---

#### 💬 챗봇 실행 화면 및 히스토리 화면

| **챗봇 실행 화면**                                                                 | **챗봇 히스토리 화면**                                                         |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| ![챗봇 실행 화면 GIF](https://github.com/user-attachments/assets/dac23602-4c9e-4e16-bbac-5084855f10a8) | ![챗봇 히스토리 화면](https://github.com/user-attachments/assets/1de032fb-4b2a-4fd7-a329-75759601621a) |

---

챗봇은 실행 화면에서 다양한 대화 기능을 제공하며, 히스토리 화면에서는 대화 이력을 관리할 수 있습니다.
챗봇은 사용자에게 더 나은 경험을 제공하기 위해 지속적으로 업데이트됩니다.

---

## 🛠 트러블 슈팅 및 성능 개선

### 📌 RAG를 이용한 챗봇

| **문제**                                                                                  | **원인**                                                                                   | **해결**                                                                                 | **결과**                                 |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------|
| **문제 1** : 정형 데이터를 벡터 임베딩하여 벡터DB 이용 시 검색 정확도 낮음                   | DB 통일 및 OpenSearch 벡터 서치 사용                                                       | 벡터를 임베딩하지 않고 쿼리문으로 조회하는 공정 추가                                       | "안정적인 정형 데이터 RAG 구조 형성"     |
| **문제 2** : OpenSearch 쿼리문 생성 후 실행 시 오류 발생                                    | 생성된 쿼리문의 컬럼명에 띄어쓰기나 `/` 등이 포함되었을 때 오류 발생                        | MySQL에서 변수명에 백틱(`)을 추가하여 띄어쓰기 및 특수문자를 올바르게 처리                 | "보다 정확한 DB 조회 가능"               |

---

### 🚀 성능 개선

| **항목**                              | **필요성**                                                                 | **해결 방안**                                                                        | **결과**                                     | **이미지**                                                                                  |
|---------------------------------------|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------|----------------------------------------------|---------------------------------------------------------------------------------------------|
| **성능 개선 1** : 각 차트 요약문 개선  | 데이터프레임을 프롬프트로 전달할 경우 행간 의미를 정확히 이해하지 못함        | 쿼리 결과를 데이터프레임이 아닌 JSON 형식으로 전달                                    | "인사이트 도출 성공"                         | ![차트 요약문 성능 개선](https://github.com/user-attachments/assets/f72b7b53-550c-4c71-bbe0-308a2ce359d7) |
| **성능 개선 2** : 게시판 기능 구현     | 공지사항 및 Q&A 게시판 부재로 사용자 피드백 창구 부족                        | Django에 `blog` 앱 추가를 통해 사용자 게시판 기능 구현                                | 사용자 문의 증가로 운영 부담 감소 및 만족도 향상 | ![게시판 기능 구현](https://github.com/user-attachments/assets/8cae8aac-c054-4ce6-815e-19b231386629)       |

---

### 상세 설명
1. **성능 개선 1**  
   데이터 분석 과정에서 프롬프트로 데이터를 전달할 때 JSON 형식으로 변환하여 인사이트를 명확히 도출할 수 있도록 개선했습니다.
   
2. **성능 개선 2**  
   게시판을 통해 공지사항, Q&A 및 사용자 피드백을 효율적으로 관리하며 사용자 만족도와 참여도를 높였습니다.

위의 개선 사항은 사용자 경험 향상과 효율적인 운영에 기여하고자 진행되었습니다.


---

위의 트러블 슈팅과 성능 개선은 사용자 경험 향상 및 시스템 안정성을 도모하고자 진행되었습니다.



## 개발 성과 평가 
![image](https://github.com/user-attachments/assets/ffa48468-41e2-41dc-ab14-a4a1fde72196)


## 💡 현직자 피드백과 그에 따른 개선 방향

### 🔍 주요 피드백

1. **정확성 및 피드백 루프 부족**  
   - **문제**: 챗봇이 제공한 결과에 대한 실질적 반응률 및 성과 피드백 부족.  
   - **해결 제안**: 
     - 실 데이터와의 비교 검증 과정 추가.
     - 사용자 설문 또는 반응 데이터를 활용한 성과 분석 도입.

2. **알고리즘 다양성 및 최신 트렌드 반영 필요**  
   - **문제**: 특정 알고리즘(Facebook Prophet 등)에 대한 의존성 지적.  
   - **해결 제안**: 
     - 다양한 예측 모델 비교 검토.
     - 최신 트렌드 반영 및 적합성 검토.

3. **보안 및 규제 고려 필요**  
   - **긍정적**: 금융 생성형 AI 보안 규제에 대한 사전 고려는 인상적임.  
   - **추가 제안**: 
     - 금융감독원의 최신 규제 및 데이터 편향성 검토 반영.
     - 프로젝트에 구체적인 보안 검토 내용 추가.

4. **사용자 반응 데이터 활용**  
   - **문제**: 단순한 ‘좋아요/싫어요’ 버튼 피드백만으로는 부족함.  
   - **해결 제안**: 
     - 사용자 설문, 기프트콘 등 보상을 통한 피드백 유도.
     - 이벤트 효과에 대한 정량적 데이터 수집 및 분석.

---

### 📈 피드백을 통한 개선 방향
1. **사용자 중심 사례 추가**: 페르소나를 기반으로 한 구체적 시나리오 및 사례 시연 강화.  
2. **성과 검증 프로세스 도입**: 실 데이터 비교, 반응률 분석, 사용자 피드백 수집 강화.  
3. **알고리즘 다양화**: 다양한 예측 모델 활용 및 최신 트렌드 반영.  
4. **보안 및 규제 준수 강화**: 금융 보안 규제와 데이터 편향성 검토 내용 반영.  
5. **사용자 피드백 루프 강화**: 반응 데이터를 수집하여 지속적인 개선에 활용.

---

### 🏆 총평
- **긍정적 요소**: 챗봇의 기획 및 구현 방향성에 대한 긍정적 평가.  
- **추가 개선 필요성**: 사용자 피드백 및 데이터 기반 성과 검증 프로세스 보완.  
- **기대 효과**: 현업에 도입 시 높은 활용 가능성 기대.

---

### ✍️ 추가 참고
- 금융감독원 2023년도 금융 생성형 AI 보안 가이드 참고.
- 알고리즘 비교 연구: Facebook Prophet 외 최신 예측 모델 검토.
- 사용자 피드백 활성화 방안: 설문 조사, 보상 체계 활용.




## 프로젝트 후기
### 신호섭 후기 
```
이 프로젝트는 열정적인 팀원들과 함께 협업하며 얻은 정말 소중한 경험이었습니다. 프로젝트를 통해 다양한 기술과 도구를 활용하면서 성공적인 결과물을 만들어낼 수 있었습니다.
주요 기술 및 프로세스
1. Prophet 모델 활용을 통한 경제 지표 예측
* Prophet 모델을 적용하여 경제 지표를 예측하는 과정을 다루며, 데이터 분석 및 모델링 역량을 강화할 수 있었습니다.
2. Django 프레임워크로 웹페이지 구현
* Django 프레임워크를 사용해 웹페이지를 개발하며 백엔드와 프론트엔드 간의 유기적인 연결을 경험할 수 있었습니다.
3. Docker와 Git 활용
* Docker를 이용해 효율적인 개발 환경을 구성하고, Git을 통해 협업을 원활히 진행하며 팀 프로젝트의 생산성을 높일 수 있었습니다.
4. Airflow를 활용한 데이터 파이프라인 구성
* 공공데이터 API를 통해 데이터를 주기적으로 수집 및 DB에 적재하는 파이프라인을 구축하였고, 이를 기반으로 대시보드의 그래프를 최신화할 수 있도록 설정했습니다.
5. 챗봇 기능 개발
* Django 프레임워크에서 JavaScript와 Views 파일 간의 연동을 통해 다음과 같은 기능을 구현했습니다:
페이지 세션 ID를 활용한 사용자 히스토리 기능
챗봇의 Thumb's Up/Down 기능: 사용자의 피드백(+1/-1)을 DB에 반영하여 챗봇의 성능을 모니터링하고 개선 가능성을 분석할 수 있었습니다.

* 금융 도메인 지식 습득
특히, 프로젝트를 통해 금융 도메인에 대한 지식을 쌓을 수 있었던 점이 매우 큰 성과였습니다. 금융 데이터를 다루며 도메인 특성과 관련된 데이터 처리 및 분석 기술의 중요성을 배울 수 있었습니다.

* 결론
이 프로젝트는 기술적인 성장뿐 아니라 팀원들과의 협업 능력 및 커뮤니케이션 스킬을 키울 수 있었던 매우 귀중한 시간이었습니다. 다양한 기술 스택을 활용해 문제를 해결하고, 결과물을 성공적으로 완성함으로써 프로젝트의 성취감을 깊이 느낄 수 있었습니다.
```

### 조진원 후기
```
첫 AI 개발 프로젝트를 통해 많은 것을 배웠습니다. 

첫 번째로 얻은 것은 기술적 성장입니다. 프로젝트 전에는 파이썬을 사용해 단순한 예측 모델을 구축하는 것이 한계였지만, 이번 프로젝트를 통해 Docker를 통한 통합 개발 환경 구축, Git을 활용한 협업 및 체계적 프로젝트 관리, MySQL 및 OpenSearch를 통한 정형 및 비정형 데이터의 통합 관리와 활용, Airflow를 이용한 자동화 체계 구축, 그리고 AWS 클라우드 서비스를 이용한 배포 시스템 구축까지 다양한 기술 스택을 다룰 수 있게 되었습니다. 이를 통해 전반적인 개발 체계에 대한 깊은 이해를 가지게 되었습니다. 또한 생성형 AI와 머신러닝 및 딥러닝 모델을 통해 분석을 고도화하여 고객 맞춤형 서비스를 구축하면서, 데이터 처리, 시스템, 분석을 아우르는 종합적인 AI 엔지니어링 역량을 크게 향상시킬 수 있었습니다.

두 번째로 얻은 것은 팀원 간의 협업 경험입니다. 이 프로젝트에서는 실제 실무에서 경험할 수 있는 요구 사항 정의서를 분석하여 각자의 역할을 명확히 하고, 진행 상황을 Slack과 Notion을 통해 기록 및 공유함으로써 효율적인 분업 체계를 구축하였습니다. 이 경험을 통해 체계화 및 문서화의 중요성을 다시금 깨닫게 되었습니다. 무엇보다 팀원 간의 적극적인 의사소통을 통한 복잡한 문제 해결 경험은 제 협업 역량을 크게 키워주었습니다.

이번 프로젝트는 저에게 단순 분석 및 기획에 그쳤던 저의 역량을 그 기획한 것을 실제 비즈니스 영역에 구현 및 적용할 수 있게 해주는 매우 뜻깊은 경험이었습니다.
```

### 박은채 후기 
```
많은 것을 배울 수 있었던 소중한 시간이었습니다. 팀 프로젝트를 마무리하며 팀원들 간에 누구도 감정 상하지 않고 원만하게 끝낼 수 있어 큰 만족을 느낍니다. 각자 맡은 분야를 작업하고 이를 합치는 과정에서 많은 오류와 의견 차이가 있었지만, 오전과 오후에 진행한 회의를 통해 의견을 잘 조율할 수 있었고, 이 점에서 팀원들에게 깊은 감사함을 느낍니다.

프로젝트의 효율성을 높이기 위해 통합 환경을 구축하여 환경의 일관성과 확장성을 확보하는 데 주력했으며, 이를 통해 협업의 장점을 실감할 수 있었습니다. 다만, 기한 내 구현에 집중하다 보니 작업 과정을 체계적으로 기록하지 못한 점이 아쉽지만, 이번 프로젝트를 통해 많은 것을 배우고 느낄 수 있었습니다. 함께한 팀원들 모두 고생 많으셨습니다.
```

### 정지연 후기
```
‘우대리’ 프로젝트는 단순한 챗봇 개발이 아니라, 실제 업무의 불편함을 해결하는 경험이었습니다. 처음엔 PLM이라는 도메인이 생소하고 복잡했지만, 하나씩 구조를 파악하고 팀원들과 흐름을 도식화하며 실마리를 찾았습니다. 자연어로 데이터를 조회하고, 자동으로 수집·시각화되는 시스템을 만들어가면서 기술이 실무를 어떻게 바꿀 수 있는지 체감할 수 있었습니다. 특히 서로 다른 배경을 가진 팀원들과 협업하며, 기획과 개발 사이를 조율하는 과정에서 커뮤니케이션의 중요성도 크게 느꼈습니다. 결과적으로는 최우수상을 받았지만, 그보다 더 값진 건 제가 만든 서비스가 실제 현장의 문제를 해결할 수 있다는 확신이었습니다.
```

### 이은지 후기 
```
이번 프로젝트를 통해 정말 많은 것을 배웠습니다. Git을 활용한 협업은 물론, 주간 회의를 통해 작업물을 공유하고 방향성을 조율하는 과정은 팀워크의 중요성을 다시금 깨닫게 해주었습니다. 특히, 서버와 Docker를 이용한 협업은 실무에서의 경험을 쌓는 데 큰 도움이 되었습니다.

기획과 데이터 분석에 그치지 않고 실제 서비스에 맞춰 웹 서버를 구축한 것은 이 프로젝트의 가장 큰 성과 중 하나였습니다. 모델 학습부터 시작해 버전 관리를 위한 모델 서빙, 데이터 자동 추출 시스템까지, 우리가 만든 시스템은 실제 서비스와 매우 유사한 환경을 제공했습니다. 이러한 경험은 앞으로의 경력에 큰 자산이 될 것입니다.

또한, 프로젝트 전반에 걸쳐 팀원 간의 협력이 돋보였습니다. 마지막까지 서로 도우며 큰 마찰 없이 진행할 수 있었던 점이 특히 인상 깊었습니다. 이번 프로젝트는 단순한 학습을 넘어, 실질적인 경험과 팀워크의 가치를 느낄 수 있는 소중한 기회였습니다.
```


