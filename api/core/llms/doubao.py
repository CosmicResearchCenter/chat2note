from volcenginesdkarkruntime import Ark
from volcenginesdkarkruntime.types.chat import ChatCompletionMessage,ChatCompletionSystemMessageParam,ChatCompletionUserMessageParam,ChatCompletionAssistantMessageParam,ChatCompletionRole,ChatCompletionMessageParam
from typing import List,Iterable

from configs.llm_config import llm_Settings

from .llm import LLM
class DouBaoLLM(LLM):
    def __init__(self,api_key:str=llm_Settings.DOUBAOAI_API_KEY,base_url:str=llm_Settings.DOUBAOAI_BASE_URL,model:str=llm_Settings.DOUBAOAI_MODEL) -> None:
        self.client = Ark(api_key=api_key,base_url=base_url)
        self.messages:List[Iterable[ChatCompletionMessageParam]]= []
        self.model:str = model

    def setPrompt(self,prompt:str):
        message:ChatCompletionSystemMessageParam = ChatCompletionSystemMessageParam(role="system",content=prompt) 
        self.messages.append(message)
    def addHistory_User(self,content):
        message:ChatCompletionUserMessageParam = ChatCompletionUserMessageParam(role="user",content=content) 
        self.messages.append(message)
    def addHistory_Assistant(self,content):
        message:ChatCompletionAssistantMessageParam = ChatCompletionAssistantMessageParam(role="assistant",content=content)
        self.messages.append(message)
    def addHistory(self, messages):
        self.messages.extend(messages)
    def ChatToBot(self,content:str):
        self.addHistory_User(content)
        completion = self.client.chat.completions.create(
            model=self.model,
            messages = self.messages,
            stream=False,
        )
        return completion.choices[0].message.content
    def ChatToBotWithSteam(self, content: str):
        self.addHistory_User(content)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=True
        )
        for chunk in response:
            yield chunk.choices[0].delta.content
if __name__ == "__main__":
    
    doubao = DouBaoLLM()
    doubao.setPrompt("你是一个聊天助手")
    # print(doubao.ChatToBot("你好"))
    rs = doubao.ChatToBotWithSteam("你好")
    for r in rs:
        print(r)