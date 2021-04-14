a = int(input("월 입력:"))

samsipill = [1, 3, 7, 8, 10, 12]
samsip = [4, 6, 9, 11]

if a == 2:  # 파이썬은 switch 없음
    print("28")
elif a in samsip:
    print("30")
elif a in samsipill:
    print("31")


# 딕셔너리 이용하기
def switch(i):
    return {1: 31, 2: 28, 3: 31}.get(i, -1)  # 키 값에 해당하는 것이 없으면


print(switch(a))
