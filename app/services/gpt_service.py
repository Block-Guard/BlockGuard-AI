from openai import OpenAI, OpenAIError
from app.config.setting import settings
from app.models.fraud_request import FraudRequest
from app.prompts.fraud_prompts import get_fraud_detection_prompt

client = OpenAI(
    api_key = settings.gpt_api_key
    )

async def call_gpt(request: FraudRequest):
    messages = get_fraud_detection_prompt(
        message_content = request.messageContent, 
        additional_description = request.additionalDescription
    )
    
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input = messages,
            temperature = 0.5, # 생성된 텍스트의 무작위성을 결정
            max_output_tokens = 200
        )
        print(response.output_text.strip())
        
    except OpenAIError as e:
        raise RuntimeError(f"GPT API 호출 실패: {e}")
    except Exception as e:
        return f"서버 오류 발생: {e}"

    return response.output_text.strip()
