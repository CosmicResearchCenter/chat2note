from database.mysql_client import MysqlClient
from models.llm_info import Api_Keys
class OpenAI_Config(MysqlClient):
    API_KEY:str = ""
    BASE_URL:str= ""
    MODEL:str= ""
    
    def __init__(self) -> None:
        super().__init__()
        self.getinfo()
    def __del__(self):
        super().__del__()
    def getinfo(self):
        info = self.db.query(Api_Keys).filter(Api_Keys.provider == "OPENAI").first()
        if info:
            self.API_KEY = info.api_key
            self.BASE_URL = info.config['BASE_URL']
            self.MODEL = info.config['MODEL']
            return
        print("没有配置OPENAI API信息")
        return
        

class ZhiPuAI_Config(MysqlClient):
    API_KEY:str= ""
    MODEL:str= ""
    def __init__(self) -> None:
        super().__init__()
        self.getinfo()
    def getinfo(self):
        info = self.db.query(Api_Keys).filter(Api_Keys.provider == "ZHIPUAI").first()
        if info:
            self.API_KEY = info.api_key
            self.MODEL = info.config['MODEL']
            return
        print("没有配置ZHIPUAI API信息")
        return
        
class SparkAI_Config(MysqlClient):
    APP_ID:str= ""
    API_SECRET:str= ""
    API_KEY:str= ""
    BASE_URL:str= ""
    DOMAIN:str= ""
    def __init__(self) -> None:
        super().__init__()
        self.getinfo()
    def __del__(self):
        super().__del__()
    def getinfo(self):
        info = self.db.query(Api_Keys).filter(Api_Keys.provider == "SPARKAI").first()
        if info:
            self.API_KEY = info.api_key
            self.APP_ID = info.config['APP_ID']
            self.API_SECRET = info.config['API_SECRET']
            self.BASE_URL = info.config['BASE_URL']
            self.DOMAIN = info.config['DOMAIN']
            return
        print("没有配置SPARKAI API信息")
        return
        
class DouBaoAI_Config(MysqlClient):
    API_KEY:str= ""
    BASE_URL:str= ""
    MODEL:str= ""
    def __init__(self) -> None:
        super().__init__()
        self.getinfo()
    def __del__(self):
        super().__del__()
    def getinfo(self):
        info = self.db.query(Api_Keys).filter(Api_Keys.provider == "DOUBAO").first()
        if info:
            self.API_KEY = info.api_key
            self.BASE_URL = info.config['BASE_URL']
            self.MODEL = info.config['MODEL']
            return
        print("没有配置DOUBAOAI API信息")
        return
        
       
class LLM_Settings:
    OPENAI_API_KEY: str= ""
    OPENAI_BASE_URL: str= ""
    OPENAI_MODEL: str= ""

    ZHIPUAI_API_KEY: str= ""
    ZHIPUAI_MODEL: str= ""

    SPARKAI_APP_ID: str= ""
    SPARKAI_API_SECRET: str= ""
    SPARKAI_API_KEY: str= ""
    SPARKAI_BASE_URL: str= ""
    SPARKAI_DOMAIN: str= ""


    DOUBAOAI_API_KEY: str= ""
    DOUBAOAI_BASE_URL: str= ""
    DOUBAOAI_MODEL: str= ""
    
    
    def __init__(self):
        self.get_llm_info()

    def get_llm_info(self):
        openai = OpenAI_Config()
        sparkai = SparkAI_Config()
        zhuziai = ZhiPuAI_Config()
        doubaoai = DouBaoAI_Config()
        
        self.OPENAI_API_KEY = openai.API_KEY
        self.OPENAI_BASE_URL = openai.BASE_URL
        self.OPENAI_MODEL = openai.MODEL
        
        self.SPARKAI_API_SECRET = sparkai.API_SECRET
        self.SPARKAI_API_KEY = sparkai.API_KEY
        self.SPARKAI_APP_ID = sparkai.APP_ID
        self.SPARKAI_BASE_URL = sparkai.BASE_URL
        self.SPARKAI_DOMAIN = sparkai.DOMAIN
        
        self.ZHIPUAI_API_KEY = zhuziai.API_KEY
        self.ZHIPUAI_MODEL = zhuziai.MODEL
        
        self.DOUBAOAI_API_KEY = doubaoai.API_KEY
        self.DOUBAOAI_BASE_URL = doubaoai.BASE_URL
        self.DOUBAOAI_MODEL = doubaoai.MODEL

llm_Settings = LLM_Settings()
   
if __name__ == "__main__":
    openAI_Config = OpenAI_Config()
    print(openAI_Config.API_KEY)