from enum import Enum
from .doubao import DouBaoLLM
from .openaillm import OpenAILLM
from .zhipuai_llm import ZhiPuAI_LLM
from .sparkai_llm import SparkAILLM
from .llm import LLM

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
        if lLM_Provider == LLM_Provider.DOUBAO:
            return DouBaoLLM()
        elif lLM_Provider == LLM_Provider.OPENAI:
            return OpenAILLM()
        elif lLM_Provider == LLM_Provider.ZHIPUAI:
            return ZhiPuAI_LLM()
        elif lLM_Provider == LLM_Provider.SPARKAI:
            return SparkAILLM()
        else:
            raise Exception("Not supported mode_provider type")
        
if __name__ == "__main__":
    llm = LLM_Manager().creatLLM("OPENAI")
    llm.setPrompt("你是一个聊天助手")
    print(llm.ChatToBot("你好"))
    