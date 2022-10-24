'''
게임 시나리오
도라에몽이 길을 가다가 몬스터를 만남
1. 싸움 2. 도망간다
선택: 1
당신의 선택은 1번
싸움이 시작됩니다 가 출력 되게 해보자

만약에 싸운다(1)를 누르면
싸움이 시작됩니다
만약에 2번이면 도망간다

1. 주먹으로 때린다
2. 발로 찬다
3. 머리로 박는다
4. 도구를 쓴다
만약에 1번을 누르면
몬스터가 데미지를 입었다 또는 피했다
만약에 4번을 누르면 도구 리스트가 출력
1. 야구방망이
2. 사랑의 회초리
3. 막대사탕
'''

import gamemod
print("당신은 길을 가다가 괴상한 몬스터와 마주쳤다.")
print("어떻게 하면 좋을까?")
print("1. 싸운다 / 2. 도망간다")
number = input("숫자를 입력하세요: ")
print(f"당신은 {number}을 선택했다.")

# 만약에 1번이면 싸운다.
if (number=="1"):
    print("싸움이 시작됩니다.\n")
    gamemod.step1()
elif (number=="2"):
    print("당신은 도망갑니다.")
    gamemod.step2()
else:
    print("해당되는 숫자를 정확히 누르세요.\n")
    
    print("마지막 선택 기회입니다. 잘못 입력시 게임오버!")


