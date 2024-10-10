from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Any, Callable, Optional
from typing import List
from configs.config import settings
# 数据库设置
user = settings.MYSQL_USER
password = settings.MYSQL_PASSWORD
ip = settings.MYSQL_IP
port = settings.MYSQL_PORT
basename = settings.MYSQL_BASE

DATABASE_URL = f"mysql+pymysql://{user}:{password}@{ip}:{port}/{basename}"
# engine = create_engine(DATABASE_URL)
# SessionLocal = 
Base = declarative_base()

class MysqlClient:
    def __init__(self,database_url:str=DATABASE_URL):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine,expire_on_commit=False)
        self.db = self.SessionLocal()
    def __del__(self):
        self.db.close()
