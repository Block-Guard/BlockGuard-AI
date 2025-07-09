# 1. 베이스 이미지로 Python 3.9 선택
FROM python:3.9-slim

# 2. 작업 디렉토리 생성
WORKDIR /app

# 3. 요구 사항 파일 복사
COPY requirements.txt /app/

# 4. 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. 애플리케이션 코드 복사
COPY . /app/

# 6. FastAPI 서버 실행 (Uvicorn 사용)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
