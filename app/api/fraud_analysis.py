from fastapi import APIRouter, HTTPException
from app.services.gpt_service import call_gpt
from app.models.fraud_request import FraudRequest
from app.models.fraud_response import FraudResponse

router = APIRouter()

@router.post(
    path = "",
    response_model=FraudResponse,
    summary="사기 유형 분석"
)
async def fraud_analysis(request: FraudRequest):
    try:
        answer = await call_gpt(request)
        response = FraudResponse.model_validate_json(answer)
        return response
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=f"사기분석 실패: {e}") from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"응답 파싱 실패: {e}") from e
