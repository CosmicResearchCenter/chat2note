from fastapi import APIRouter
from core.chat2note.chat_type import ChatLog
from api.core.chat2note.chat2note import ChatToNote

router = APIRouter()

@router.post("/chat2note")
async def chat2note(chat:ChatLog):
    return {"note":"HelloWorld"}