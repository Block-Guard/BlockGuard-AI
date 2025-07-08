from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("")
async def fraud_analysis():
    return {"message": "사기분석 API"}