from pydantic import BaseModel
from typing import List

class FraudExample(BaseModel):
    type_name: str
    message_content: List[str]
    keywords: List[str]
    additional_description: List[str]
