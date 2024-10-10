from sqlalchemy import Column, Float, Integer, String, Text,TIMESTAMP,Boolean
from api.database.mysql_client import Base

class LLM_Info(Base):
    __tablename__ = "llm_info"

    id = Column(Integer, primary_key=True)