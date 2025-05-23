from fastapi import FastAPI

from llama import LlamaChat
from schemas import ChatInput

app = FastAPI()

@app.get("/")
async def root():
    return {"Message" : "fastAPI first programme"}

@app.post("/chat/")
async def chat(chat_input: ChatInput):
    chat = LlamaChat(
        chat_input=chat_input.input,
        exit=chat_input.exit
    )
    return {"bot": chat.response}
