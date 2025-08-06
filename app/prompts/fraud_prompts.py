from typing import List, Dict
from app.prompts.fraud_example import FraudExample
from app.prompts.data.fraud_examples import FRAUD_EXAMPLES

def get_fraud_detection_prompt(
    message_content: str,
    additional_description: str,
    keywords: List[str],
    image_content: str,
    examples: List[FraudExample] = FRAUD_EXAMPLES
) -> List[Dict[str, str]]:
    
    system = {
        "role": "system",
        "content": (
            "당신은 사기 탐지 어시스턴트입니다. "
            "입력된 텍스트를 반드시 예시 데이터로 입력된 사기 유형 중 하나로 분류하고, "
            "최소 1개에서 최대 3개의 주요 위험 키워드를 추출하며, 그 이유를 설명하고, "
            "위험 점수(0–70%)를 제공해야 합니다.\n"
            "출력은 반드시 valid JSON 객체로만 응답하세요. 아래는 응답 예시입니다:\n"
            "{\n"
            "  \"estimatedFraudType\": \"복권 사기\",\n"
            "  \"keywords\": [\"키워드1\", \"키워드2\"],\n"
            "  \"explanation\": \"...\",\n"
            "  \"score\": 62.4\n"
            "}\n"
        )
    }

    example_lines = build_example_lines(examples)
    assistant_content = "".join(example_lines)
    assistant_content += (
        "이제 아래 입력을 같은 형식으로 분류하세요:\n"
    )

    assistant = {
        "role": "assistant",
        "content": assistant_content
    }

    user = {
        "role": "user",
        "content": (
            f"messageContent: '{message_content}'\n"
            f"additionalDescription: '{additional_description}'\n"
            f"keywords: {', '.join(keywords) if keywords else 'None'}\n"
            f"imageContent: '{image_content}'"
        )
    }

    return [system, assistant, user]

def build_example_lines(examples):
    example_lines = ["사기 유형 및 예시:\n"]
    for idx, ex in enumerate(examples, start=1):
        example_lines.append(f"{idx}. {ex.type_name}:\n")
        example_lines.append(f"   messageContent: '{ex.message_content}'\n")
        example_lines.append(f"   additionalDescription: '{ex.additional_description}'\n")
        example_lines.append(f"   keywords: '{ex.keywords}'\n")
        
    return example_lines
