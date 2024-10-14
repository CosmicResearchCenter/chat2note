from typing import List,Iterable
import sys
# sys.path.append('..')
from .chat_type import ChatLog
from core.llms.llm_manager import LLM_Manager

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
    llm1 = LLM_Manager().creatLLM("openai")
    # openai = OpenAILLM(api_key=api_key,base_url=base_url,model=model)
    llm1.setPrompt("你是一个笔记撰写师")
    print("Generating note...")
    answer = llm1.ChatToBot(log_texts)
    print("Note generation complete")

    llm2 = LLM_Manager().creatLLM("openai")
    # openai1 = OpenAILLM(api_key=api_key,base_url=base_url,model=model)
    llm2.setPrompt("你是一个文件名称生成器")
    content = f"""
请你根据以下笔记内容，生成一个合适的文件名称(不要拓展名)，只要输出文件名称即可，不要包含其他内容。
以下是笔记内容：
{answer}
输出：
文件名称
    """
    print("Generating file name...")
    file_name = llm2.ChatToBot(content)
    print(f"The file name is generated, and the file name is called {file_name}")
    # 将结果保存到.md文件中
    with open(f"{file_name}.md", "w", encoding='utf-8') as file:
        file.write(answer)
    print(f"Note have been saved to {file_name}.md file")
    
 
# 两张方式
# 1. 命令行转笔记模式
    # 从环境变量中加载配置信息
# 2. 网页转笔记模式
    # 从获取从数据库获取到的配置信息


    
class ChatToNote:
    def __init__(self,provider:str) -> None:
        self.provider:str = provider

        self.llm_chat2note = LLM_Manager().creatLLM(provider)
        self.llm_file_name = LLM_Manager().creatLLM(provider)
    def prase_chat_history(self,chat_history: List[ChatLog]):
        if len(chat_history) == 0:
            raise ValueError("Chat history cannot be empty.")
        logs = ""
        for log in chat_history:
            log_text = f"""
##############
role:{log.role}
content:
{log.content}
##############
"""         
            logs += log_text
        return logs
    
    def chat_to_note(self,log_text,steaming:bool=False):
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
        log_texts += log_text

        
        # print(log_texts)

        # 调用OpenAI的LLM模型
        # llm1 = LLM_Manager().creatLLM("openai")
        # openai = OpenAILLM(api_key=api_key,base_url=base_url,model=model)
        self.llm_chat2note.setPrompt("你是一个笔记撰写师")
        print("Generating note...")
        
        if steaming == False:
            answer = self.llm_chat2note.ChatToBot(log_texts)
            print("Note generation complete")
            return answer
        else:
            answer = self.llm_chat2note.ChatToBotWithSteam(log_texts)
            for i in answer:
                yield i
        # llm2 = LLM_Manager().creatLLM("openai")
        # openai1 = OpenAILLM(api_key=api_key,base_url=base_url,model=model)
#         self.llm_file_name.setPrompt("你是一个文件名称生成器")
#         content = f"""
# 请你根据以下笔记内容，生成一个合适的文件名称(不要拓展名)，只要输出文件名称即可，不要包含其他内容。
# 以下是笔记内容：
# {answer}
# 输出：
# 文件名称
#     """
#         print("Generating file name...")
#         file_name = self.llm_file_name.ChatToBot(content)
#         print(f"The file name is generated, and the file name is called {file_name}")
        # 将结果保存到.md文件中
        # with open(f"{file_name}.md", "w", encoding='utf-8') as file:
        #     file.write(answer)
        # print(f"Note have been saved to {file_name}.md file")
            