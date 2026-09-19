from fastapi import FastAPI
from pydantic import BaseModel

from app.agent.agent import AIBinoAgent


app = FastAPI(title="AI-Bino")

agent = AIBinoAgent()


class MessageRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "AI-Bino is running",
        "status": "online"
    }


@app.post("/chat")
def chat(request: MessageRequest):
    response = agent.respond(request.message)

    return {
        "response": response
    }