"""
Chatbot API routes.
Exposes the /api/message endpoint where users can send messages,
and the bot replies based on stored intents"""
from fastapi import APIRouter
from pydantic import BaseModel
from src.services.chatbot_service import get_reply

router = APIRouter()

# request schema for /api/message
class MessageRequest(BaseModel):
    message: str

# response schema for /api/message
class MessageResponse(BaseModel):
    reply: str

@router.post("/message", response_model=MessageResponse)
def get_message(request: MessageRequest):
    """
    Endpoint: POST /api/meessage
    Input: {"message":"hello"}
    Output: {"reply": "Hi there!"}
    """
    reply = str(get_reply(request.message))
    return {"reply": reply} # not just reply
