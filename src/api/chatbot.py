from fastapi import APIRouter
from pydantic import BaseModel
from src.services.chatbot_service import get_reply

router = APIRouter()

# Request body schema
class MessageRequest(BaseModel):
    message: str

# Response schem
class MessageResponse(BaseModel):
    reply: str

@router.post("/message", response_model=MessageResponse)
def get_message(request: MessageRequest):
    # for now just echo back message
    reply = str(get_reply(request.message))
    return MessageResponse(reply=reply)