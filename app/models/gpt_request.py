from pydantic import BaseModel

class GPTRequest(BaseModel):
    prompt: str
    max_tokens: int = 150
