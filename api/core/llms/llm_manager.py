from enum import Enum
from .doubao import DouBaoLLM
from .openaillm import OpenAILLM
from .zhipuai_llm import ZhiPuAI_LLM
from .sparkai_llm import SparkAILLM
from .llm import LLM
from configs.llm_config import llm_Settings
class LLM_Provider(Enum):
    """
    Types of LLM Providers.
    """
    OPENAI = "OPENAI"
    DOUBAO = "DOUBAO"
    ZHIPUAI = "ZHIPUAI"
    SPARKAI = "SPARKAI"
    @classmethod
    def get_llm(cls, mode_provider: str):
        for member_name, member in cls.__members__.items():
            if member_name == mode_provider:
                return member
        else:
            raise Exception("Not supported mode_provider type")
    
class LLM_Manager:
    def creatLLM(self,mode_provider: str)->LLM:
        lLM_Provider = LLM_Provider.get_llm(mode_provider)
        llm_Settings.get_llm_info()
        if lLM_Provider == LLM_Provider.DOUBAO:
            return DouBaoLLM(
                        api_key=llm_Settings.DOUBAOAI_API_KEY,
                        base_url=llm_Settings.DOUBAOAI_BASE_URL,
                        model=llm_Settings.DOUBAOAI_MODEL)
        elif lLM_Provider == LLM_Provider.OPENAI:
            return OpenAILLM(
                    api_key=llm_Settings.OPENAI_API_KEY,
                    base_url=llm_Settings.OPENAI_BASE_URL,
                    model=llm_Settings.OPENAI_MODEL
                    )
        elif lLM_Provider == LLM_Provider.ZHIPUAI:
            return ZhiPuAI_LLM(
                    api_key=llm_Settings.ZHIPUAI_API_KEY,
                    model=llm_Settings.ZHIPUAI_MODEL
                    )
        elif lLM_Provider == LLM_Provider.SPARKAI:
            return SparkAILLM(
                    spark_api_key=llm_Settings.SPARKAI_API_KEY,
                    spark_api_secret=llm_Settings.SPARKAI_API_SECRET,
                    spark_llm_domain=llm_Settings.SPARKAI_DOMAIN,
                    spark_api_url=llm_Settings.DOUBAOAI_BASE_URL,
                    spark_app_id=llm_Settings.SPARKAI_APP_ID,
                    )
        else:
            raise Exception("Not supported mode_provider type")
        
if __name__ == "__main__":
    llm = LLM_Manager().creatLLM("OPENAI")
    llm.setPrompt("你是一个聊天助手")
    print(llm.ChatToBot("你好"))
    