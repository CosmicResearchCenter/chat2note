from DrissionPage import Chromium,ChromiumOptions

from typing import Any,List
from .chat_type import ChatLog
class ChatLoger:
    def __init__(self,url:str):
        self.co = ChromiumOptions().headless()
        self.browser = Chromium(self.co)
        self.page = self.browser.latest_tab
        self.page.get(url)
    def get_log_user(self)->List[ChatLog]:
        print("Retrieving user conversation history.")
        # self.page.get(url)
        texts = self.page.s_eles(".whitespace-pre-wrap")
        chatLogs:List[ChatLog] = []
        for text in texts:
            # print(text.text)
            chatLogs.append(ChatLog("user",text.text))
        print("Successfully retrieved user conversation history.")
        return chatLogs
    def get_log_assistant(self)->List[ChatLog]:
        # self.page.get(url)
        print("Retrieving AI conversation history.")
        texts = self.page.s_eles(".markdown prose w-full break-words dark:prose-invert dark")
        
        chatLogs:List[ChatLog] = []
        for text in texts:
            # print(text.text)
            chatLogs.append(ChatLog("assistant",text.text))
        print("Successfully retrieved AI conversation history.")
        return chatLogs
    def parse_log(self,chatLogs_user:List[ChatLog],chatLogs_assistant:List[ChatLog])->List[ChatLog]:
        print("Parsing conversation history")
        parsedLogs:List[ChatLog] = []
        length = len(chatLogs_user)
        i = 0
        while i < length:
            try:
                parsedLogs.append(chatLogs_user[i])
                parsedLogs.append(chatLogs_assistant[i])
                i += 1
            except Exception as e:
                print(e)
                break
        self.browser.quit()
        print("Conversation history parsing completed")
        return parsedLogs



            


if __name__ == "__main__":
    url = "https://chatgpt.com/share/67014432-b0b0-8009-8ab1-4bb026108c1e"
    loger = ChatLoger(url)
    logs_user = loger.get_log_user()
    logs_assistant = loger.get_log_assistant()

    logs = loger.parse_log(logs_user,logs_assistant)
    for log in logs:
        print(f"{log.role}: {log.content}")

