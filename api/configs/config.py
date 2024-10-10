from dotenv import load_dotenv
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MYSQL_IP: str
    MYSQL_PORT: str
    MYSQL_BASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    OPENAI_API_KEY: str
    OPENAI_BASE_URL: str
    OPENAI_MODEL: str

    ZHIPU_API_KEY: str


    SPARK_APP_ID: str
    SPARK_AAPI_SECRET: str
    SPARK_API_KEY: str
    SPARK_DOMAIN: str


    DOUBAO_API_KEY: str
    DOUBAO_BASE_URL: str
    DOUBAO_MODEL: str
    class Config:
       env_file = ".env"
    
settings = Settings()