from fastapi import APIRouter, HTTPException
from app.services.gpt_service import call_gpt

router = APIRouter()

@router.get("")
async def fraud_analysis():
    try:
        answer = await call_gpt()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"result": answer}