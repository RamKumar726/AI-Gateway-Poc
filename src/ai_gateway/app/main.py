from fastapi import FastAPI
from .api.chat import chat
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    question : str
    persona : str


@app.get("/")
def health():
    return {"Ok"}

@app.post('/ask')
def create_chat(request : Request):
    question = request.question
    persona = request.persona
    result = chat(question=question, persona_id = persona)
    return{
        "response" : result,
        "status" : 200
    }

