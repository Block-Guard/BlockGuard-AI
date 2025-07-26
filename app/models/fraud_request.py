from pydantic import BaseModel
from typing import List
from typing import Optional

class FraudRequest(BaseModel):
    messageContent: Optional[str] = None
    keywords: List[str]
    additionalDescription: Optional[str] = None
    imageContent: Optional[str] = None