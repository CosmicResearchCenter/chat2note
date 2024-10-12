from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
from configs.llm_config import llm_Settings
from typing import List,Iterable
from .llm import LLM



class SparkAILLM(LLM):
    def __init__(self, 
                 spark_api_key: str=llm_Settings.SPARKAI_API_KEY,
                 spark_api_url:str=llm_Settings.SPARKAI_BASE_URL,
                 spark_api_secret:str=llm_Settings.SPARKAI_API_SECRET,
                 spark_llm_domain:str=llm_Settings.SPARKAI_DOMAIN,
                 spark_app_id:str=llm_Settings.SPARKAI_APP_ID,
            ) -> None:
        self.client = ChatSparkLLM(spark_api_key=spark_api_key,spark_api_secret=spark_api_secret,spark_app_id=spark_app_id,spark_llm_domain=spark_llm_domain,spark_api_url=spark_api_url)
        self.messages: List[ChatMessage] = []

    def setPrompt(self, prompt: str):
        message =ChatMessage(role="system", content=prompt)
        self.messages.append(message)
        
    def addHistory_User(self, content: str):
        message = ChatMessage(role="user", content=content)
        self.messages.append(message)

    def addHistory_Assistant(self, content: str):
        message = ChatMessage(role="assistant", content=content)
        self.messages.append(message)
    def addHistory(self, messages: List[ChatMessage]):
        self.messages.extend(messages)
    def ChatToBot(self, content: str):
        self.addHistory_User(content)
        handler = ChunkPrintHandler()
        a = self.client.generate([self.messages], callbacks=[handler])
        
        return a.generations[0][0].text
    def ChatToBotWithSteam(self, content: str):
        self.addHistory_User(content)
        handler = ChunkPrintHandler()
        self.client.streaming = True
        response = self.client.generate([self.messages], callbacks=[handler])
        print(type(response))
        return response
if __name__ == "__main__":
    llm = SparkAILLM()
    llm.setPrompt("你是谁")
    a = llm.ChatToBotWithSteam("你是谁")
    print(a)