# 취미클래스 플랫폼(Class 101, 탈잉, 클래스톡) 별 비교
## : 취미생활∙자기계발 트렌드를 반영한 검색/추천시스템
#### CRAWLING PROJECT
#### - Period: 2021. 02. 22. ~ 2021. 03.19.
#### - 인원 : 2명
#### - Member: 고원진, 장지혜
<br/>


![플랫폼](https://user-images.githubusercontent.com/75402257/109494745-a6324d00-7ad1-11eb-86a8-675130405701.png)
<br/>

## 1. Intro

### 1-1.

![취미](https://user-images.githubusercontent.com/75402257/109493201-7b46f980-7acf-11eb-8855-40666dccf54e.png)

- 주 52시간 근무제 시행으로 늘어난 여가시간을 풍요롭게 하는 취미플랫폼의 급성장 

- 코로나로 늘어난 '집콕족'들의 라이프스타일 변화

- 다양한 관심사와 자기계발을 돕는 온라인/오프라인 플랫폼 수요증가
 
### 1-2.

-

-


<br/>

![예상](https://user-images.githubusercontent.com/75402257/110046690-d9096900-7d8f-11eb-89e6-6fa1be4234bd.PNG)

<br/>

## 2. Goals

- 세 개 플랫폼 데이터를 Mysql DB 저장 및 키워드 분류
- 소비자가 필요한 클래스 정보를 키워드 검색을 통해 얻을 수 있는 검색엔진 구현
 - 웹 서비스 제공

## 3. Result

- 
- 
- 



## 4. Process

### I. Crawling Method1
- Class101(클래스101) : Jquery (수정필)
- Taling(탈잉) : Scrapy -> BeautifulSoup 으로 크롤링 방식 변경
   -(Category_1, Category_2 분류 -> 키워드검색)
- ClassTok(클래스톡) : Scrapy -> BeautifulSoup   

### II. DataBase
- Mysql (RDBMS): 검색/키워드 추천을 위한 인덱싱의 중요성
- Flask를 통한 서비스 구현을 위한 DB 연동 (업데이트)
- Backup DB에 관한 논의 필

### III. Crawling Cycle

- 실시간성을 높이기 위해 6시간 간격 (하루 3번 정도 업데이트 : 클래스톡, 탈잉의 경우)
   - 매일 1시간 간격 or 매일 1회 크롤링을 통한 데이터 수집내용 비교
   - Mysql에는 기존 데이터 지우고 업데이하는 형식으로 크롤링 진행중
   - csv 포맷으로도 축적중 
   
- 서버를 늘려서 실시간성 증대 
   - 각 서비스별 정보만은 text로 제공시 서버를 분산하지 않아도 된다는 판단

## 5. Issue
### 5-1. keyword 분류
- Mysql - like : DB, tag 컬럼 추가(구분자)
- 해시태그, 태그 같이 저장 -> DB (중복검색 가능성 염두에 두고 태그 나누기)

<br/>


## 4. Process
- 데이터 수집 (웹 사이트 크롤링)
- DB 저장 : SQLAlchemy -> Mysql(RDBMS) 
- 데이터 성능검사 (검색키워드)
- Flask - DB 연동


### I. Crawling Method

- Class101(클래스101) : Jquery (수정필)
- Taling(탈잉) : Scrapy -> BeautifulSoup 으로 크롤링 방식 변경
   -(Category_1, Category_2 분류 -> 키워드검색)
- ClassTok(클래스톡) : Scrapy -> BeautifulSoup   


<br/>

### II. DataBase

![RRRRR](https://user-images.githubusercontent.com/75402257/111388988-9468c080-86f3-11eb-8f39-e59c8e5bf4b5.PNG)

- Mysql (RDBMS): 검색/키워드 추천을 위한 인덱싱의 중요성
- Flask를 통한 서비스 구현을 위한 DB 연동 (업데이트)
- Backup DB에 관한 논의 필


### III. Crawling Cycle
- 실시간성을 높이기 위해 6시간 간격 (하루 3번 정도 업데이트 : 클래스톡, 탈잉의 경우)

   - 매일 1시간 간격 or 매일 1회 크롤링을 통한 데이터 수집내용 비교
   - Mysql에는 기존 데이터 지우고 업데이하는 형식으로 크롤링 진행중
      - 데이터 축적되는 방식으로 변경 
   - csv 백업형태로 저장


- 서버를 늘려서 실시간성 증대 
   - 각 서비스별 정보만은 text로 제공시 서버를 분산하지 않아도 된다는 판단

<br/>

## 5. Issue

- 키워드 검색 정확도 (모델 성능검사)
- 

### 5-1. keyword 분류

![CCCC](https://user-images.githubusercontent.com/75402257/111389073-b06c6200-86f3-11eb-86f0-117682482f4b.PNG)

- Mysql - like : DB, tag 컬럼 추가(구분자)

- 해시태그, 태그 같이 저장 -> DB (중복검색 가능성 염두에 두고 태그 나누기)

- 정확한 키워드 검색을 위한 자연어 처리 및 문자열 형태소분류
  - 차후 학습이 더 진행된 상태에서 Develop 논의
  - 
### 5-2. 서비스 구현

![FF](https://user-images.githubusercontent.com/75402257/111388270-54550e00-86f2-11eb-9c8b-cb320b8f1b37.PNG)
- Flask를 이용해서 서비스 구현가능: 검색/추천 시스템(키 값 별도로 빼기)
  - Flask - DB 연동


<br/>

### Member / role

- **고원진** / 탈잉, 클래스 101 웹크롤링, DB연동(Mysql),
- **장지혜** / 탈잉, 클래스톡 웹크롤링, 웹서비스(Flask), 

<br/>



### Data 출처

- [클래스101] (https://class101.net/)
- [탈잉] (https://taling.me/)
- [클래스톡] (https://www.classtok.net/)



<br/>



### Reference


##### 기사
- 이정화 (2020. 06. 22.). “[TDI 데이터 나우] 취미클래스 플랫폼 인기몰이, 새로운 문화로 자리잡다”. <미라클어헤드>.
  - URL: https://mirakle.mk.co.kr/view.php?year=2020&no=637941
- 이준형 (2020. 01. 23.). “[기획의 건축] 클래스 101앱은 어떻게 생겼을까?”. <모비인사이드>.
  - URL: https://www.mobiinside.co.kr/2020/01/23/planning-uxui/
- Captin (2020. 12. 24.). “[스타트업 BM 분석] 취미플랫폼 4곳 BM분석- 최초,클래스101이 아닙니다”. <모비인사이드>.
  - URL: https://www.mobiinside.co.kr/2020/12/24/hobby-platform/



##### 논문 및 보고서
-

-


