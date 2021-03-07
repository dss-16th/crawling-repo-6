
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:dss@52.78.38.124/crawling_project?charset=utf8", encoding='utf-8')

# 테이블 객체 생성을 위한 클래스 작성
Base = declarative_base()

class User(Base):
    
    __tablename__ = "class101" # 테이블 이름
    
    # 컬럼 데이터 작성
    site = Column(String(30))
    link = Column(String(30), primary_key=True)
    title = Column(String(30))
    teacher = Column(String(20))
    category_1 = Column(String(20))
    category_2 = Column(String(20))
    s_price = Column(String(20))
    discount = Column(String(20))
    contentment = Column(String(20))
    
    # 생성자 함수
    def __init__(self, site, link, title, category_1, category_2, s_price, discount, contentment):
        self.site = site
        self.link = link
        self.title = title
        self.category_1 = category_1
        self.category_2 = category_2
        self.s_price = s_price
        self.discount = discount
        self.contentment = contentment
        
    # repr 함수
    def __repr__(self):
        return "<User {}, {}, {}, {}, {}, {}, {}, {}>".format(
        self.site, self.link, self.title, self.category_1, 
        self.category_2, self.s_price, self.discount, self.contentment)
    

# engine에 연결된 데이터 베이스(test)에 테이블 생성
Base.metadata.create_all(engine)

# 데이터 베이스에 session 연결
Session = sessionmaker(engine)
session = Session()
session

classtok_df.to_sql(name='classtok', con=engine, if_exists='replace')
