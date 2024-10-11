from sqlalchemy import Column, Float, Integer, String, Text,TIMESTAMP,Boolean,JSON
from database.mysql_client import Base

class Api_Keys(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True)
    provider = Column(String(255))
    api_key = Column(String(255)) 
    config = Column(JSON)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP) 