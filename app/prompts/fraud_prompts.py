from typing import List, Dict
from pathlib import Path
from app.prompts.fraud_example import FraudExample
from app.prompts.data.fraud_examples import FRAUD_EXAMPLES

SYSTEM_PROMPT = """
너는 보이스피싱 사기 탐지 전문가다.
다음 규칙표를 사용해 입력 텍스트를 분석하고,
1) 사기 유형(카테고리) 선택
2) 핵심 키워드(최소1~최대3) 추출
3) 점수는 최소 0점에서 최대 70점

[점수 규칙]
- 규칙표는 "카테고리ID 카테고리명" 한 줄 + 그 아래 여러 룰 라인으로 구성된다.
- 룰 라인 형식: "룰ID:배점:키워드1|키워드2|...".
- 'messageContent', 'keywords', 'additionalDescription'에 해당 룰의 키워드 중 1개라도 의미/표현상 해당 룰에 해당된다면 판단하면 그 룰의 배점을 가산(룰별 최대 1회).
- 'imageContent'는 유형 분류에 참고할 것.
- 유저가 입력한 'keywords', 'additionalDescription'에 매칭되는 키워드가 있으면 점수 계산.
- 규칙표의 각자 룰들의 키워드들의 유사성을 분석하고, 유사한 키워드도 해당 룰에 매칭여부를 관대하게 판단할 것을 명심해라.
- 키워드는 의미가 같으면 띄어쓰기/대소문자/오타 등과 동의어 허용.
- 동일 카테고리에서 여러 룰이 적중할 수 있으며, 합산 후 카테고리 점수는 70을 초과하지 않는다.
- 최종적으로 가장 점수가 높은 카테고리를 estimatedFraudType으로 선택.
- 동점이면 적중 룰 개수가 더 많은 카테고리를 선택. 그래도 동률이면 의미상 더 근접한 쪽.
- 링크/단축URL은 http/https, bit.ly/han.gl/is.gd/vo.la/me2.do 등도 매칭으로 본다(표기 변형 허용).

출력은 반드시 valid JSON 객체로만 응답. 오직 JSON만 출력. 
코드블록(```), 주석, 추가 텍스트, 설명 모두 금지.
'estimatedFraudType' 에는 오로지 카테고리명만 넣을 것.
아래는 응답 예시.
{
  "estimatedFraudType": "<카테고리명>",
  "keywords": ["<키워드1>", "<키워드2>", "<키워드3>"],
  "explanation": "<왜 이 유형이고 어떤 이유로 판단하였는지 간결히 설명>",
  "score": <0~70의 실수값>
}

""".strip()

def _load_rules() -> str:
    rules_path = Path(__file__).parent / "data" / "score_rules.txt"
    return rules_path.read_text(encoding="utf-8")

def get_fraud_detection_prompt(
    message_content: str,
    additional_description: str,
    keywords: List[str],
    image_content: str,
    examples: List[FraudExample] = FRAUD_EXAMPLES
) -> List[Dict[str, str]]:
    rules_text = _load_rules()
    example_text = "".join(build_example_lines(examples))


    system = {
        "role": "system",
        "content": f"{SYSTEM_PROMPT}\n\n[규칙표]\n{rules_text}\n\n[예시]\n{example_text}"
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

    return [system, user]


def build_example_lines(examples):
    example_lines = ["사기 유형 및 예시:\n"]
    for idx, ex in enumerate(examples, start=1):
        example_lines.append(f"{idx}. {ex.type_name}:\n")
        example_lines.append(f"   messageContent: '{ex.message_content}'\n")
        example_lines.append(f"   additionalDescription: '{ex.additional_description}'\n")
        example_lines.append(f"   keywords: '{ex.keywords}'\n")
        
    return example_lines