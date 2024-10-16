from core.chat2note.chat2note import ChatToNote
from core.chat2note.get_logs import ChatLoger
from models.llm_info import Api_Keys
from database.mysql_client import MysqlClient
from datetime import datetime
class Chat2NoteService:
    def __init__(self,provider:str) -> None:
        self.chatToNote = ChatToNote(provider)
        
    def chat_to_note(self,url:str,steaming:bool=False):
        chatLoger = ChatLoger(url)
        
        chatLogs_user = chatLoger.get_log_user()
        chatLogs_assistant = chatLoger.get_log_assistant()
        chatLogs = chatLoger.parse_log(chatLogs_user,chatLogs_assistant)
        
        log_text = self.chatToNote.prase_chat_history(chatLogs)
        if not steaming:
            res = self.chatToNote.chat_to_note(log_text,steaming)
        
            return res
        else:
            res = self.chatToNote.chat_to_note(log_text,steaming)
            for i in res:
                # i = i.replace('\n', '\\n')
                print(i)
                if i:
                    yield i
    def chat_to_note_test(self,text,steaming:bool=False):
        if not steaming:
            res = self.chatToNote.chat_to_note(text,steaming)
        elif steaming:
            res = self.chatToNote.chat_to_note(text,steaming)
            for i in res:
                print(i)
                # i = i.replace('\n', '\\n')
                yield f"data:{i}"
        # for i in res:
        #     print(i)
class ProviderService(MysqlClient):
    def __init__(self) -> None:
        super().__init__()
        pass
    def get_provider_list(self):
        Info =  self.db.query(Api_Keys).all()
        providers = []
        for i in Info:
            providers.append(i.provider)
        return providers
    def set_provider(self,provider:str,api_key,config)->bool:
        item = self.db.query(Api_Keys).filter(Api_Keys.provider==provider).first()
        if item:
            item.api_key = api_key
            item.config = config
            timestamp = datetime.now()
            item.updated_at = timestamp
            self.db.commit()
            self.db.refresh(item)
            return True
        else:
            timestamp = datetime.now()
            llm_info = Api_Keys(provider=provider,api_key=api_key,config=config, created_at=timestamp,updated_at=timestamp)
            print(llm_info.id)
            self.db.add(llm_info)
            self.db.commit()
            self.db.refresh(llm_info)
        return True
if __name__ == "__main__":
    # ch = Chat2NoteService("OPENAI")
    # ch.chat_to_note("https://chatgpt.com/share/670cefb4-0ae8-8009-b0a2-609e20541598",steaming=True)
    provider = ProviderService()
    print(provider.get_provider_list())