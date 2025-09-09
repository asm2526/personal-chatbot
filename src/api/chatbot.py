from fastapi import APIRouter
from pydantic import BaseModel

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
    return {"reply": f"You said: {request.message}"}