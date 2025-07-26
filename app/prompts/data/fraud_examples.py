from typing import List
from app.prompts.fraud_prompts import FraudExample

# 여기에 18개 유형 × 3~4개 예시만큼 리스트를 정의
FRAUD_EXAMPLES: List[FraudExample] = [
    FraudExample(
        type_name="피싱",
        message_content="귀하의 계정이 잠길 수 있습니다. 비밀번호를 확인하려면 여기를 클릭하세요.",
        additional_description="늦은 밤, 낯선 번호로 온 SMS를 우연히 열어보았습니다.",
        keywords=["계정 잠금", "비밀번호 확인", "SMS 링크"],
        image_content="은행알림 Bot: 당신의 계좌가 비정상적으로 활동되어 잠길 예정입니다. https://bit.ly/secure-link"
    ),
    FraudExample(
        type_name="투자 사기",
        message_content="2주 만에 30% 수익 보장! 지금 투자하세요.",
        additional_description="점심시간 카페에서 친구가 공유한 링크를 클릭했습니다.",
        keywords=["30% 수익", "지금 투자", "보장된 수익"],
        image_content="InvestPro: 한정 시간 30% 수익, 투자하기 ▶ http://invest.example.com"
    ),
    FraudExample(
        type_name="복권 사기",
        message_content="축하합니다! 당신은 1,000,000달러에 당첨되었습니다. 수수료를 지불하면 수령 가능합니다.",
        additional_description="출근길 지하철에서 받은 이메일에 포함된 링크를 클릭했습니다.",
        keywords=["당첨", "수수료", "이메일 링크"],
        image_content="LotteryKingdom: Congratulations! You've won $1,000,000. Click here https://lotto.fake/claim"
    ),
    # … (총 60~70개 항목)
]
