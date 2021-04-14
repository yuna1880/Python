b = True

i = 0
f = 0.
# s = ""
s = ''

s = '' # 파이선은 "와 '가 같다.
print(type(b),type(i), type(f), type(s))

i = 200 + 200
print(i)

j = i + 100
print(j)

i = j + 300
print(i, j)

i = i + 100
print(i)

# 파이썬은 증감연산자가 없습니다.
# ++i
# print(i)

k = 0 # 선언필수
print(k)

myVar = 100
print(type(myVar))
myVar += 0.1
# 0.1 을 더해준 순간 타입이 변한다.
print(type(myVar))