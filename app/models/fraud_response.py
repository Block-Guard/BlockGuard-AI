from pydantic import BaseModel, conint
from typing import List

class FraudResponse(BaseModel):
    fraud_type: str                  # 분류된 사기 유형
    keywords: List[str]              # 주요 위험 키워드 (최대 3개)
    reason: str                      # 해당 유형으로 판단한 이유
    risk_score: float                  # 위험도(0~100)