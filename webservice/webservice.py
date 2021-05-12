from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True, DEBUG=True)

# Setting Mysql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dss@52.78.38.124:3306/crawled'
mysql_db = SQLAlchemy(app)

class Crawling(mysql_db.Model):
    
    __tablename__ = 'search'
        
    site = mysql_db.Column(mysql_db.String(30), nullable=False)
    link = mysql_db.Column(mysql_db.String(100), primary_key=True)
    title = mysql_db.Column(mysql_db.String(200), nullable=False)
    teacher = mysql_db.Column(mysql_db.String(50), nullable=False)
    category_1 = mysql_db.Column(mysql_db.String(20), nullable=False)
    category_2 = mysql_db.Column(mysql_db.String(20), nullable=False)
    s_price = mysql_db.Column(mysql_db.String(20), nullable=False)
    discount = mysql_db.Column(mysql_db.String(20), nullable=False)
    contentment = mysql_db.Column(mysql_db.String(20), nullable=False)
    crawling_time = mysql_db.Column(mysql_db.String(20), nullable=False)

    def __init__(self, site, link, title, category_1, category_2, s_price, discount, contentment, crawling_time):
        self.site = site
        self.link = link
        self.title = title
        self.category_1 = category_1
        self.category_2 = category_2
        self.s_price = s_price
        self.discount = discount
        self.contentment = contentment
        self.crawling_time = crawling_time

mysql_db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=['GET', 'POST'])
def search():
    result = {} 

 # 문장 가져오기
    sentence = request.values.get('sentence') # 요청을 했을때 키값이 'sentence'인 내용을 받아오는 코드
    result['sentence'] = sentence
    
    # MYSQL에서 데이터 가져오기
    results = Crawling.query.filter(Crawling.title.like('%' + sentence + '%') | Crawling.category_1.like('%' + sentence + '%') | Crawling.category_2.like('%' + sentence + '%')).all()
    datas = []
    for data in results:
        datas.append({
            'site': data.site,
            'link': data.link,
            'title': data.title,
            'teacher': data.teacher,
            'category_1': data.category_1,
            'category_2': data.category_2,
            's_price': data.s_price,
            'discount': data.discount,
            'contentment': data.contentment,
        })

    print(datas)
    
    result['datas'] = datas
    
    
    
    # save mysql
#     search_history = Crawling(site, link, title, category_1, category_2, s_price, discount, contentment, crawling_time)
#     mysql_db.session.add(search_history)
#     mysql_db.session.commit()
    
    
    return jsonify(result)

app.run()
