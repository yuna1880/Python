# scanner 대신 사용 가능한 input() -> 전부 문자열(string)으로 처리한다
# a = input()
# b = input()

# string -> int 형변환
a = int(input())
b = int(input())
print(a + b)

# 에러가 뒤늦게 나온다. (컴파일러 언어가 아니라, 돌려봐야 안다)
#print(a - b)