
<br/>



![메인](https://user-images.githubusercontent.com/75402257/113556709-d3759c00-9637-11eb-9c71-286c13806d29.jpg)


<br/>

# 취미클래스 플랫폼(Class 101, 탈잉, 클래스톡) 통합 검색 웹페이지 
## : 취미생활∙자기계발 트렌드를 반영한 검색서비스 제공
<br/>

#### CRAWLING PROJECT
#### - Period: 2021. 02. 22. ~ 2021. 03.19.
#### - 인원 : 2명
#### - Member: 고원진, 장지혜


<br/>

# 0. 요약

[발표자료](https://drive.google.com/file/d/115hO8CLumxuyMbc66uCjQSXwbjKOlA1n/view?usp=sharing)

### 0-1. 3개 취미 강좌 사이트(class101, taling, classtok)의 강좌 제목 / 강사 / 카테고리 / 가격 / 별점 등 crawling
```python
 query = [{"operationName":"InfiniteProductCardsWithLastUpdatedInformation", .............}]
 req = requests.post(url_graphql, json=query, )
 datas = req.json()
```
   - class101: request를 이용하여 graphql data를 post방식 crawling
      - [class101_final.py](./class101_final.py)
   - taling: BeautifulSoup 을 이용하여 crawling, 카테고리 추가를 위해 MultiNomia Naive Bayesian Model을 이용한 카테고리 부여
      - [taling_final.py](./taling_final.py)
      - [MultinomiaNB_model](./model.py)
   - classtok: BeautifulSoup 을 이용하여 crawling
      - [classtok_final.py](./classtok_final.py)

### 0-2. crawling 정보 AWS 서버의 mysql에 저장
```python
# 데이터 베이스에 session 연결
Session = sessionmaker(engine)
session = Session()
session

class101_df.to_sql(name='class101', con=engine, if_exists='replace')
```
   - [class101_mysql_unified.py](./Database_Mysql/class101_mysql_unified.py)
   - [classtok_mysql_unified.py](./Database_Mysql/classtok_mysql_unified.py)
   - [taling_mysql_unified.py](./Database_Mysql/taling_mysql_unified.py)

### 0-3. Flask / nginx 를 활용한 웹페이지 제작
   - [Flask_web_mysql_search.ipynb](./Flask_web_mysql_search.ipynb)

### 0-4. 검색기능 구현
```python
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=['GET', 'POST'])
def search():
    result = {} 

 # 문장 가져오기
    sentence = request.values.get('sentence') # 요청을 했을때 키값이 'sentence'인 내용을 받아오는 코드
    result['sentence'] = sentence
```
   - [webservice.py](./webservice/webservice.py)

### 0-5. 웹 서비스 제공
```html
 <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
 <script type="text/javascript">
     $(document).ready(function(){
         $(".search").on("click", function(){
             var sentence = $('.sentence').val();
             var url='/search?sentence=' + sentence;

             $.getJSON(url, function(response){
                 console.log(response.datas);
                 var tag = "";
                 for (var i=0; i< response.datas.length; i++){
                     tag += '<tr>';
                     tag += '    <td>' + i + '</td>';
                     tag += '    <td>' + response.datas[i].site + '</td>';
                     tag += '    <td>' + response.datas[i].title + '</td>';
                     tag += '    <td>' + response.datas[i].category_1 + '</td>';
                     tag += '    <td>' + response.datas[i].category_2 + '</td>';
                     tag += '    <td>' + response.datas[i].s_price + '</td>';
                     tag += '    <td>' + response.datas[i].discount + '</td>';
                     tag += '    <td>' + response.datas[i].contentment + '</td>';
                     tag += '    <td>' + response.datas[i].link + '</td>';
                     tag += '</tr>';
                 }
                 $(".table tbody").html(tag);
             })
         })

     })
 </script>
```
   - [index.html](./webservice/templates/index.html)

<br/>

## 1. Intro

### 주제 선정 및 프로젝트 방향

![취미](https://user-images.githubusercontent.com/75402257/109493201-7b46f980-7acf-11eb-8855-40666dccf54e.png)

### 1-1. 취미생활/자기계발 수요증가
##
- 주 52시간 근무제 시행으로 늘어난 여가시간을 풍요롭게 하는 취미플랫폼의 급성장 

- 코로나로 늘어난 '집콕족'들의 라이프스타일 변화
<br/>

![dd](https://user-images.githubusercontent.com/75402257/113546956-fd26c700-9627-11eb-90a3-3178cd817761.PNG)
 
<br/>

### 1-2. 취미생활/자기계발 플랫폼의 성장세
##
- 다양한 관심사와 자기계발을 돕는 온라인/오프라인 플랫폼 수요증가

- N잡러, 프리랜서 마켓으로서의 역할


<br/>

![예상](https://user-images.githubusercontent.com/75402257/110046690-d9096900-7d8f-11eb-89e6-6fa1be4234bd.PNG)

<br/>

## 2. Goals

- 세 개 플랫폼 데이터를 Mysql DB 저장 및 키워드 분류
- 소비자가 필요한 클래스 정보를 키워드 검색을 통해 얻을 수 있는 검색서비스 웹으로 구현
- Database 관리 및 업데이트(실시간성 반영)

<br/>

## 3. Result

- DB 데이터 축적 및 신규강좌 업데이트
- 웹 서비스 제공, 도메인 (http://findmyclass.ml/) 생성

<br/>

## 4. Process

- 주제 선정
- 프로젝트 목적 논의
- 데이터 수집 (Crontab을 이용한 크롤링주기 설정, 자동화)
- DB 저장 : SQLAlchemy -> Mysql(RDBMS) 
- 데이터 성능검사 (검색키워드)
- Flask - DB 연동 

<br/>

### I. Crawling Method
##
- Class101(클래스101) : selenium -> graphql post방식 requests
- Taling(탈잉) : Scrapy -> BeautifulSoup 으로 크롤링 방식 변경
   -(Category_1, Category_2 분류 -> 키워드검색)
- ClassTok(클래스톡) : Scrapy -> BeautifulSoup   
<br/>


### II. DataBase
##
- Mysql (RDBMS): 검색/키워드 추천을 위한 인덱싱의 중요성
- Flask를 통한 서비스 구현을 위한 DB 연동 (업데이트)
- Backup DB에 관한 논의 필

<br/>

![RRRRR](https://user-images.githubusercontent.com/75402257/111388988-9468c080-86f3-11eb-8f39-e59c8e5bf4b5.PNG)

<br/>

![디비](https://user-images.githubusercontent.com/75402257/113553916-711a9c80-9633-11eb-8d57-7d6663a0f343.PNG)

<br/>

### III. Crawling Cycle
##
- 실시간성을 높이기 위해 6시간 간격 (하루 3번 정도 업데이트 : 클래스톡, 탈잉의 경우)
   - 매일 1시간 간격 or 매일 1회 크롤링을 통한 데이터 수집내용 비교
   - Mysql에는 기존 데이터 지우고 업데이하는 형식에서 데이터 축적하는 방식으로 변경 (백업 DB)
   - 초기에는 csv 형태로 데이터를 축적하였으나 DB에 축적하는 방식으로 변경
   
- 서버를 늘려서 실시간성 증대 필요성 논의
   - 각 서비스별 정보를 text형태로만 제공시 서버를 분산하지 않아도 된다는 판단

- 신규강좌 부분 추가
   - 크롤링 시간을 기준으로 3일 전 데이터 삭제
   - 신규강좌 데이터 확인 후 업데이트

<br/>

## 5. Service Implementation Method
### 5-1. keyword 분류
##
- 형태소 분류의 필요성 논의
  - 차후 학습진행 후 Develop 논의
- Mysql - like : DB, tag 컬럼 추가(구분자)
- 카테고리 분류, 해시태그, 태그 같이 저장 -> DB (중복검색 가능성 염두에 두고 태그 나누기)
- 검색 정확도 (MultinomialNB 모델 사용, 모델 성능검사 test 진행)
- 정확한 키워드 검색을 위한 자연어 처리 및 문자열 형태소분류 필요성
  - 차후 학습이 더 진행된 상태에서 Develop 논의 

<br/>

### 5-2. Web Service
##
- [웹사이트 구현] (http://findmyclass.ml/)
<br/>

![플라스크 구현](https://user-images.githubusercontent.com/75402257/113553372-a5418d80-9632-11eb-917c-9757a8b856c3.PNG)


<br/>


![바탕](https://user-images.githubusercontent.com/75402257/113555260-98726900-9635-11eb-824a-c277fbf3fd91.jpg)

<br/>


![웹페이지연동](https://user-images.githubusercontent.com/75402257/113761280-3e1afa80-9752-11eb-8bd4-79e9a0197846.PNG)

<br/>



### 5-3. Model 성능평가
##
![모델성능검사](https://user-images.githubusercontent.com/75402257/113555256-96a8a580-9635-11eb-952e-aa2a2646ef8a.jpg)
 
- 과적합 가능성 염두 
- 카테고리 분류를 세분화하여 재분류 후  Model 성능평가 계획 
##

 <br/>


![이후](https://user-images.githubusercontent.com/75402257/113556165-09665080-9637-11eb-824c-889624fa6923.PNG)


<br/>


### Member / role
##
- **고원진** / 탈잉, class101 웹크롤링, 웹서비스&UI(Flask), 검색-DB연동(Mysql), 발표 및 검토, 총괄
- **장지혜** / 클래스톡 웹크롤링, 웹페이지 디자인(javascript), 발표자료 준비

<br/>



### Data 출처
##
- [클래스101] (https://class101.net/)
- [탈잉] (https://taling.me/)
- [클래스톡] (https://www.classtok.net/)



<br/>



### Reference
##
##### 기사
- 이정화 (2020. 06. 22.). “[TDI 데이터 나우] 취미클래스 플랫폼 인기몰이, 새로운 문화로 자리잡다”. <미라클어헤드>.
  - URL: https://mirakle.mk.co.kr/view.php?year=2020&no=637941
- 이준형 (2020. 01. 23.). “[기획의 건축] 클래스 101앱은 어떻게 생겼을까?”. <모비인사이드>.
  - URL: https://www.mobiinside.co.kr/2020/01/23/planning-uxui/
- Captin (2020. 12. 24.). “[스타트업 BM 분석] 취미플랫폼 4곳 BM분석- 최초,클래스101이 아닙니다”. <모비인사이드>.
  - URL: https://www.mobiinside.co.kr/2020/12/24/hobby-platform/

<br/>


##
####  ※ 본 프로젝트는 패스트캠퍼스 '데이터 사이언스 취업완성스쿨 16기', 크롤링 프로젝트로 진행되었습니다.
