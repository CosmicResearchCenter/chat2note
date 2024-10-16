from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MYSQL_IP: str
    MYSQL_PORT: str
    MYSQL_BASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    class Config:
       env_file = ".env"
       extra = 'allow'
 
settings = Settings()