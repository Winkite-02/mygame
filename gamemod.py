def step1():
    print("어떤 방식으로 맞설까?")
    print("1.주먹으로 때린다. / 2.발로 찬다. / 3.머리로 박는다. / 4.도구를 쓴다.")
    number = input("숫자를 입력하세요: ")
    print(f"당신은 {number}을 선택했다.\n")

    if (number=="4"):
        print("어떤 도구를 사용할까?")
        print("1.야구방망이\n2.사랑의 회초리\n3.막대사탕")
        number = input("숫자를 입력하세요: ")
        print(f"당신은 {number}을 선택했다.")
    else:
        print("당신의 신체 일부가 어긋나버렸다.")
# 만약에 2번이면 도망간다.
def step2():
    print("도망간다")