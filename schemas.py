from pydantic import BaseModel


class ChatInput(BaseModel):
    input: str
