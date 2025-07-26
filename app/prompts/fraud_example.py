from pydantic import BaseModel
from typing import List

class FraudExample(BaseModel):
    type_name: str
    message_content: str
    keywords: List[str]
    additional_description: str
    image_content: str