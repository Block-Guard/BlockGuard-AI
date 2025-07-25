from openai import OpenAI
from app.config.setting import settings

client = OpenAI(
    api_key = settings.gpt_api_key
    )

async def call_gpt_with_image():
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {
                    "role": "developer",
                    "content": "너는 사기분석 AI야. 사용자의 말을 토대로 사기 유형을 판단하고 그렇게 생각한 이유를 말해줘"
                },
                {
                    "role": "user",
                    "content": "나의 딸이 다른 번호로 연락이 와서 핸드폰 수리 요금을 이체해달라고 해."
                }
            ]
        )
        print(response)
    
    except Exception as e:
        return f"GPT API 호출 실패: {e}"

    return response.output_text
