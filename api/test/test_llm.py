from core.chat_log.get_logs import ChatLoger
from core.chat_log.translate_to_note import ChatToNote


url = "https://chatgpt.com/share/67014432-b0b0-8009-8ab1-4bb026108c1e"
loger = ChatLoger(url)
logs_user = loger.get_log_user()
logs_assistant = loger.get_log_assistant()

logs = loger.parse_log(logs_user,logs_assistant)
for log in logs:
    print(f"{log.role}: {log.content}")
    
chat2note = ChatToNote("OPENAI")
chat2note.chat_to_note(logs)