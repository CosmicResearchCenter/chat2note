from openai import OpenAI
from openai.types.chat import ChatCompletionToolParam,ChatCompletionToolChoiceOptionParam
# import openai
from typing import List,Iterable
import sys
# sys.path.append('..')
from .chat_type import ChatLog

class OpenAILLM:
    def __init__(self, api_key: str,base_url:str,model:str) -> None:
        if not api_key:
            raise ValueError("API key is required.")
        if not base_url:
            raise ValueError("Base URL is required.")
        if not model:
            raise ValueError("Model name is required.")
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

    def ChatToBot(self, content: str):
        self.addHistory_User(content)
        response = self.client.chat.completions.create(
            model=self.model ,
            messages=self.messages
        )
        message_content = response.choices[0].message.content
        self.addHistory_Assistant(message_content)
        return message_content

# 聊天记录转换成笔记
def chat_to_note(chat_history: List[ChatLog],api_key: str,base_url:str,model:str):
    if len(chat_history) == 0:
        raise ValueError("Chat history cannot be empty.")
    if not api_key or not base_url or not model:
        raise ValueError("API key, Base URL and Model are required.")
    # 解析聊天记录
    log_texts = """
请根据以下聊天对话内容，总结出一份简洁的笔记。并以Markdown格式输出。
聊天记录格式如下：
##############
role: {log.role}
content:
{log.content}
##############
请直接输出Markdown格式的笔记，不要包含其他内容。
以下是聊天记录：

"""


    for log in chat_history:
        log_text = f"""
##############
role:{log.role}
content:
{log.content}
##############
        """
        log_texts += log_text
    # print(log_texts)

    # 调用OpenAI的LLM模型
    openai = OpenAILLM(api_key=api_key,base_url=base_url,model=model)
    openai.setPrompt("你是一个笔记撰写师")
    print("Generating note...")
    answer = openai.ChatToBot(log_texts)
    print("Note generation complete")

    openai1 = OpenAILLM(api_key=api_key,base_url=base_url,model=model)
    openai1.setPrompt("你是一个文件名称生成器")
    content = f"""
请你根据以下笔记内容，生成一个合适的文件名称(不要拓展名)，只要输出文件名称即可，不要包含其他内容。
以下是笔记内容：
{answer}
输出：
文件名称
    """
    print("Generating file name...")
    file_name = openai1.ChatToBot(content)
    print(f"The file name is generated, and the file name is called {file_name}")
    # 将结果保存到.md文件中
    with open(f"{file_name}.md", "w", encoding='utf-8') as file:
        file.write(answer)
    print(f"Note have been saved to {file_name}.md file")
    
