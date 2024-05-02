import random

# 무작위 답
random_responses = ["꽤 흥미롭네요, 자세히 알려주세요.",
                    "알겠어요. 계속하세요.",
                    "왜 그런 말을 하세요?",
                    "정말 웃긴 날씨죠?",
                    "주제를 바꿔 봅시다.",
                    "어젯밤에 경기 보셨나요?"]

print("안녕하세요 심플로봇 마빈 입니다.")
print("언제든지 '안녕'을 입력하여 이 대화를 종료할 수 있습니다.")
print("각 답변을 입력한 후 'Enter'를 누르세요.")
print("오늘 기분이 어떠세요?")

while True:
    # 상대방의 답변 입력
    user_input = input("> ")
    if user_input.lower() == "잘가":
        # 잘가라고 입력 시 대화 종료
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("대화해서 즐거웠어요. 안녕!")
