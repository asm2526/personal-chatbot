from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import chatbot, intent

app = FastAPI(title="Algo Chatbot")

# Allow React frontend (http://localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(chatbot.router, prefix="/api")
app.include_router(intent.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to Algo Chatbot"}
