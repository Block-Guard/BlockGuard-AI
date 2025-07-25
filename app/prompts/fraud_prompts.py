from typing import List, Dict

def get_fraud_detection_prompt(
    message_content: str,
    additional_description: str
) -> List[Dict[str, str]]:
    system = {
        "role": "system",
        "content": (
            "당신은 사기 탐지 어시스턴트입니다. "
            "입력된 텍스트를 반드시 미리 정의된 사기 유형 중 하나로 분류하고, "
            "최소 1개에서 최대 3개의 주요 위험 키워드를 추출하며, 그 이유를 설명하고, "
            "위험 점수(0–100%)를 제공해야 합니다.\n"
            "출력은 반드시 valid JSON 객체로만 응답하세요. 아래는 응답 예시입니다:\n"
            "{\n"
            "  \"estimatedFraudType\": \"복권 사기\",\n"
            "  \"keywords\": [\"키워드1\", \"키워드2\"],\n"
            "  \"explanation\": \"...\",\n"
            "  \"score\": 92.4\n"
            "}\n"
        )
    }

    assistant = {
        "role": "assistant",
        "content": (
            "사기 유형 및 예시:\n\n"
            "1. 피싱:\n"
            "   messageContent: '귀하의 계정이 잠길 수 있습니다. 비밀번호를 확인하려면 여기를 클릭하세요.'\n"
            "   additionalDescription: '늦은 밤, 낯선 번호로 온 SMS를 우연히 열어보았습니다.'\n"
            "   출력 JSON 예시:\n"
            "   {\n"
            "     \"estimatedFraudType\": \"피싱\",\n"
            "     \"keywords\": [\"계정이 잠길\", \"비밀번호 확인\"],\n"
            "     \"explanation\": \"긴급성을 조성하며 비밀번호 확인 링크를 제공하는 전형적인 피싱 패턴입니다.\",\n"
            "     \"score\": 88.5\n"
            "   }\n\n"
            "2. 투자 사기:\n"
            "   messageContent: '2주 만에 30% 수익 보장! 지금 투자하세요.'\n"
            "   additionalDescription: '점심시간 카페에서 친구가 공유한 링크를 클릭했습니다.'\n"
            "   출력 JSON 예시:\n"
            "   {\n"
            "     \"estimatedFraudType\": \"투자 사기\",\n"
            "     \"keywords\": [\"30% 수익 보장\", \"지금 투자\"],\n"
            "     \"explanation\": \"높은 수익을 짧은 기간에 보장한다는 과장된 약속이 전형적인 투자 사기 신호입니다.\",\n"
            "     \"score\": 90.2\n"
            "   }\n\n"
            "이제 다음 입력을 같은 형식으로 분류하세요:\n"
        )
    }

    user = {
        "role": "user",
        "content": (
            f"messageContent: '{message_content}'\n"
            f"additionalDescription: '{additional_description}'"
        )
    }

    return [system, assistant, user]
