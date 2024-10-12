class ChatLog:
    role: str = ""
    content: str = ""
    def __init__(self,role:str="",content:str=""):
        self.role = role
        self.content = content