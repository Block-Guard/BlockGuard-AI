from fastapi import APIRouter, HTTPException
from app.services.gpt_service import call_gpt_with_image

router = APIRouter()

@router.get("")
async def fraud_analysis():
    try:
        answer = await call_gpt_with_image()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"result": answer}