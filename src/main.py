from fastapi import FastAPI

app = FastAPI(title="Algo Chatbot")

@app.get("/")
def root():
    return {"message": "Welcome to Algo Chatbot 🚀"}
