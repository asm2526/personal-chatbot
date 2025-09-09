"""
Main FastAPI application entrypoint
Initializes the app, configures CORS, and registers routers
"""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import chatbot, intent

# initialize fastAPI app
app = FastAPI(title="Algo Chatbot")

# Allow React frontend (http://localhost:3000)
# Allow requests from React frontent running on port 3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(chatbot.router, prefix="/api")
app.include_router(intent.router, prefix="/api")

@app.get("/")
def root():
    """
    Health check/root endpoint"""
    return {"message": "Welcome to Algo Chatbot"}
