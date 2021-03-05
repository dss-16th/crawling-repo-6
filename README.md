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

-
-

## 3. Result

- 
- 
- 
<br/>

## 4. Process
### I. Crawling Method
- Class101(클래스101) : Jquery (수정필)
- Taling(탈잉) : Scrapy
- ClassTok(클래스톡) : BeautifulSoup / Scrapy (크롤링 방식에 따라 start_now, content 수가 달라짐)

### II. DataBase
- Mysql
- DB로 옮겨서 link 쪼개기 

### III. Crawling Cycle

- 실시간성을 높이기 위해 6시간 간격 (하루 3번 정도 업데이트 : 클래스톡, 탈잉의 경우)
- 서버를 늘려서 실시간성 증대

## 5. Issue
### 5-1. keyword 분류
- Mysql - like : DB, tag 컬럼 추가(구분자)
- 해시태그, 태그 같이 저장 -> DB (중복검색 가능성 염두에 두고 태그 나누기)
- Flask를 이용해서 서비스 구현가능: 검색/추천 (키 값 별도로 빼기)



### Member / role

- **고원진** / 클래스 101 웹크롤링,
- **장지혜** / 탈잉, 클래스톡 웹크롤링,

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


