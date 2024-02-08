import random
ans = random.randint(1,100)

print("숫자 맞추기 (1~100)")
count = 0
while count < 7:
    num = int(input("숫자를 입력하세요 : "))
    if num == ans:
        print(f"정답입니다! 답 : {num}")
        print(f"{count}번만에 맞춤")
        break
    elif num > ans:
        print("추측한 수가 답보다 큽니다")
    else:
        print("추측한 수가 답보다 작습니다")
    count += 1