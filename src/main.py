from fastapi import FastAPI
from src.api import chatbot, intent

app = FastAPI(title="Algo Chatbot")

app.include_router(chatbot.router, prefix="/api")
app.include_router(intent.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to Algo Chatbot 🚀"}
