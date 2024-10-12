from openai import OpenAI
from zhipuai import ZhipuAI
# import openai
from typing import List,Iterable
import sys
# sys.path.append('..')
from configs.llm_config import llm_Settings
from .llm import LLM

class ZhiPuAI_LLM(LLM):
    def __init__(self, api_key: str=llm_Settings.ZHIPUAI_API_KEY,model:str=llm_Settings.ZHIPUAI_MODEL) -> None:
        self.client = ZhipuAI(api_key=api_key) # 填写您自己的APIKey
        self.messages: List[Iterable[dict]] = []
        self.model = model

    def setPrompt(self, prompt: str):
        message = {"role": "system", "content": prompt}
        self.messages.append(message)
        
    def addHistory_User(self, content: str):
        message = {"role": "user", "content": content}
        self.messages.append(message)

    def addHistory_Assistant(self, content: str):
        message = {"role": "assistant", "content": content}
        self.messages.append(message)
    def addHistory(self, messages):
        self.messages.extend(messages)
    def ChatToBot(self, content: str):
        self.addHistory_User(content)
        response = self.client.chat.completions.create(
            model=self.model,  # 填写需要调用的模型编码
            messages=self.messages,
        )
        message_content=response.choices[0].message.content
        return message_content
    def ChatToBotWithSteam(self, content: str):
        self.addHistory_User(content)
        response = self.client.chat.completions.create(
            model=self.model,  # 填写需要调用的模型编码
            messages=self.messages,
            stream=True,
        )
        for chunk in response:
            yield chunk.choices[0].delta.content
if __name__ == "__main__":
   
    # print(LLM_Settings)
    openai1 = ZhiPuAI_LLM()
    openai1.setPrompt("你是一个聊天助手")
    # print(openai1.ChatToBot("秦始皇是谁"))
    rs = openai1.ChatToBotWithSteam("秦始皇是谁")
    for r in rs:
        print(r)
    