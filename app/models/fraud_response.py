from pydantic import BaseModel, Field
from typing import List

class FraudResponse(BaseModel):
    estimatedFraudType: str                  # 분류된 사기 유형
    keywords: List[str] = Field(default_factory=list, max_items=3, description="주요 위험 키워드 (최대 3개)")
    explanation: str                      # 해당 유형으로 판단한 이유
    score: float = Field(..., ge=0, le=70, description="위험도(0~70)")