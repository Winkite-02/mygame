import mod1

num1 = 10
num2 = 5

# 더하기
result = mod1.add(num1, num2)
# 결과값 출력
print(result)

# 두 수를 입력 받게 만들고
# 메뉴1. 더하기 2. 빼기
# 만약에 1을 누르면 두 수의 더한 결과값
# 만약에 2를 누르면 두 수의 뺀 결과값
# 출력되게 해보자

import mod1

num1 = int(input("첫 번째 수를 입력하세요: ")) #문자로 입력되기 때문에 숫자로 입력
print(f"당신은 {num1}을 입력했습니다.")
num2 = int(input("두 번째 수를 입력하세요: ")) #문자로 입력되기 때문에 숫자로 입력
print(f"당신은 {num2}를 입력했습니다.")

print("1.더하기 / 2.빼기")
menu = input("두 메뉴 중 해당되는 하나의 숫자를 입력하세요: ")
print(f"당신은 {menu}을 선택했습니다.")

if (menu=="1"):
    result = mod1.add(num1, num2)
    print("결과값: ", result)
elif (menu=="2"):
        result = mod1.sub(num1, num2)
        print("결과값: ", result)
else:
    print("해당되는 숫자를 정확히 누르세요.")

