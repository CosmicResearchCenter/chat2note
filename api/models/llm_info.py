from sqlalchemy import Column, Float, Integer, String, Text,TIMESTAMP,Boolean,JSON
from database.mysql_client import Base
from sqlalchemy.sql import func

class Api_Keys(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, autoincrement=True)
    provider = Column(String(255))
    api_key = Column(String(255)) 
    config = Column(JSON)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    title = Column(String(255))
    content = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class NoteList(Base):
    __tablename__ = "note_lists"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    title = Column(String(255))
    url = Column(String(255))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)