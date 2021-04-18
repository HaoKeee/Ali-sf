from sqlalchemy import Table,MetaData,create_engine,Column,String,Integer,Boolean,TIMESTAMP,func
from sqlalchemy.orm import scoped_session,sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey
import pymysql


Base = declarative_base()
DB_CONNECT_STR = "mysql+pymysql://root:@localhost:3306/Ali_sf?charset=utf8"
engine = create_engine(DB_CONNECT_STR,echo=True,encoding="utf8",convert_unicode=True)  #已更改为在pipelines中创建
db_session = scoped_session(sessionmaker(autocommit=False,  # 已更改为在pipelines中创建
                                         autoflush=False,
                                         bind=engine))
                                         
class Info(Base):
    __tablename__ = 'items_info'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(255),nullable=True)
    start_time = Column(TIMESTAMP(),nullable=True)
    end_time = Column(TIMESTAMP(),nullable=True)
    price_ratio = Column(String(255),nullable=True)
    final_status = Column(String(255),nullable=True)
    detail_url = Column(String(255),nullable=True)
    aution_times = Column(String(255),nullable=True)  #拍卖次数
    aution_mode = Column(String(255),nullable=True)
    aution_period = Column(String(255),nullable=True)
    delay_period = Column(String(255),nullable=True)
    markup = Column(String(255),nullable=True)
    starting_price = Column(String(255),nullable=True)
    margin = Column(String(255),nullable=True)
    evaluation = Column(String(255),nullable=True)
    disposal_court = Column(String(255),nullable=True)
    first_purchaser = Column(String(255),nullable=True)
    contactor = Column(String(255),nullable=True)
    phone = Column(String(255),nullable=True)
    aution_name = Column(String(255),nullable=True)
    power_source = Column(String(255),nullable=True)
    warrant_status = Column(String(255),nullable=True)
    lot_owner = Column(String(255),nullable=True)
    lot_status = Column(String(255),nullable=True)
    rights_restrictions = Column(String(255),nullable=True)
    approval_docs = Column(String(255),nullable=True)
    other_info = Column(String(255),nullable=True)
    image_url_1 = Column(String(255),nullable=True)
    image_url_2 = Column(String(255),nullable=True)
    image_url_3 = Column(String(255),nullable=True)
    image_url_4 = Column(String(255),nullable=True)
    image_url_5 = Column(String(255),nullable=True)
    image_url_6 = Column(String(255),nullable=True)
    image_url_7 = Column(String(255),nullable=True)
    image_url_8 = Column(String(255),nullable=True)
    image_url_9 = Column(String(255),nullable=True)
    image_url_10 = Column(String(255),nullable=True)
    source = Column(String(255),nullable=False,server_default='阿里拍卖')
    updated_date = Column(TIMESTAMP(),nullable=True,server_default=func.now())

    province_id = Column(Integer,ForeignKey('province.id'),nullable=False)
    type_id = Column(Integer,ForeignKey('type.id'),nullable=False)

class Type(Base):
    __tablename__ = 'type'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    id = Column(Integer,primary_key=True)
    type = Column(String(255),nullable=False)

class Province(Base):
    __tablename__ = 'province'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    id = Column(Integer,primary_key=True)
    province_name = Column(String(255),nullable=False)



def main():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()
