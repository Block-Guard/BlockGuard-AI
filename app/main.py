from fastapi import FastAPI
from app.routers import fraud_analysis

app = FastAPI()

# router 등록
app.include_router(fraud_analysis.router, prefix="/api/fraud-analysis", tags=["fraud-analysis"])

@app.get("/api/hello")
async def hello():
    return {"message": "hello world"}