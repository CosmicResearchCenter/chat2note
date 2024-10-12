from abc import ABC, abstractmethod

class LLM(ABC):
    """
    Abstract class for LLMs.
    """
    @abstractmethod
    def setPrompt(self,prompt:str):
        pass
    @abstractmethod
    def addHistory_User(self,content):
        pass
    @abstractmethod
    def addHistory_Assistant(self,content):
        pass
    @abstractmethod
    def addHistory(self,messages):
        pass
    @abstractmethod
    def ChatToBot(self,content:str):
        pass
    @abstractmethod
    def ChatToBotWithSteam(self, content: str):
        pass
