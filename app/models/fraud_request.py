from pydantic import BaseModel

class FraudRequest(BaseModel):
    user_input: str