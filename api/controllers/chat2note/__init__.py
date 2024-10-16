from fastapi import APIRouter
from starlette.responses import StreamingResponse
import time
from .models import ChatLogRequest,ChatLogResponse,ProvidersResponse,ProvidersRequest
from core.chat2note.chat2note import ChatToNote
from services.chat2note import Chat2NoteService,ProviderService
import json
router = APIRouter()

@router.post("/chat2note")
async def chat2note(chat:ChatLogRequest):
    if chat.url == "":
        return ChatLogResponse(code="400",message="url is required",data=[])
    
    if chat.steaming:
        return StreamingResponse(Chat2NoteService(chat.provider).chat_to_note(chat.url,steaming=True), media_type="text/event-stream")
    else:
        return ChatLogResponse(code="200",message="success",data=[Chat2NoteService(chat.provider).chat_to_note(chat.url)])
@router.get("/get_providers")
async def get_providers():
    provider_client = ProviderService()
    providers = provider_client.get_provider_list()
    return ProvidersResponse(code="200",message="success",data=providers)  

@router.post("/set_provider")
async def set_provider(provider:ProvidersRequest):
    
    if provider.config == "":
        return ProvidersResponse(code="400",message="config is required",data=[])
    
    if provider.provider == "":
        return ProvidersResponse(code="400",message="provider is required",data=[])
    if provider.api_key == "":
        return ProvidersResponse(code="400",message="api_key is required",data=[])
    # str to json
    config_llm = json.loads(provider.config)
    print(provider.config)
    print(config_llm)
    
    provider_client = ProviderService()
    info =  provider_client.set_provider(provider.provider,provider.api_key,config_llm)
    
    if info:
        return ProvidersResponse(code="200",message="success",data=[])
    else:
        return ProvidersResponse(code="400",message="failed",data=[])
@router.post("/test")
async def test(chat:ChatLogRequest):
    if chat.url == "":
        return ChatLogResponse(code="400",message="url is required",data=[])
    
    if chat.steaming:
        return StreamingResponse(Chat2NoteService("OPENAI").chat_to_note_test(chat.url,steaming=True), media_type="text/event-stream")
    else:
        return ChatLogResponse(code="200",message="success",data=[Chat2NoteService("OPENAI").chat_to_note_test(chat.url)])
