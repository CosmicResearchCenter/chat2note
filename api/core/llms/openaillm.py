from openai import OpenAI
# import openai
from typing import List,Iterable
import sys
# sys.path.append('..')
from configs.llm_config import llm_Settings
from .llm import LLM

class OpenAILLM(LLM):
    def __init__(self, api_key: str=llm_Settings.OPENAI_API_KEY,base_url:str=llm_Settings.OPENAI_BASE_URL,model:str=llm_Settings.OPENAI_MODEL) -> None:
        self.client = OpenAI(api_key=api_key,base_url=base_url)
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
            model=self.model ,
            messages=self.messages
        )
        message_content = response.choices[0].message.content
        self.addHistory_Assistant(message_content)
        return message_content
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
    
    # print(LLM_Settings)
    openai1 = OpenAILLM()
    openai1.setPrompt("你是一个聊天助手")
    rs = openai1.ChatToBotWithSteam("你好")
    for r in rs:
        print(r)

    