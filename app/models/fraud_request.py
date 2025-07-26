from pydantic import BaseModel
from typing import List

class FraudRequest(BaseModel):
    messageContent: str
    keywords: List[str]
    additionalDescription: str
    imageContent: str