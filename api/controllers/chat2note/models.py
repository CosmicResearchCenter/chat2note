from pydantic import BaseModel
from typing import List,Dict,Any
class ChatLogRequest(BaseModel):
    url:str
    steaming:bool=False
    
class ChatLogResponse(BaseModel):
    code:str
    message:str
    data:List[Any]