import random

a = random.randrange(1, 7) # 1 ~ 6 끝값 + 1
print(a)
b = random.randrange(1, 7)
print("A주사위 숫자는 %d 입니다." % a)
print("B주사위 숫자는 %d 입니다." % b)

if a > b:
    print("a가 이김")
elif a == b:
    print("비김")
else:
    print("b가 이김")