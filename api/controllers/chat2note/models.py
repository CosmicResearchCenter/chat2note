from pydantic import BaseModel
from typing import List,Dict,Any
class ChatLogRequest(BaseModel):
    url:str
    provider:str
    steaming:bool=False
    
class ChatLogResponse(BaseModel):
    code:str
    message:str
    data:List[Any]
class ProvidersRequest(BaseModel):
    provider:str
    api_key:str
    config:Any

class ProvidersResponse(BaseModel):
    code:str
    message:str
    data:List[Any]