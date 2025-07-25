from pydantic import BaseModel

class FraudRequest(BaseModel):
    messageContent: str
    additionalDescription: str