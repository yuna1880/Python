a = int(input("숫자 1 입력"))
b = int(input("숫자 2 입력"))

print(123456789012345678901234567890)

print("%5d%6s%6d%2s%11d" % (a,"+", b, "=", a + b))
print("%5d%6s%6d%2s%11d" % (a, "-", b, "=", a - b))
print("%5d%6s%6d%2s%11d" % (a, "*", b, "=", a * b))
print("%5d%6s%6d%2s%11d" % (a, "**", b, "=", a ** b))
print("%5d%6s%6d%2s%11.2f" % (a, "/", b, "=", a / b))
print("%5d%6s%6d%2s%11d" % (a, "//", b, "=", a // b))
print("%5d%6s%6d%2s%11d" % (a, "%", b, "=", a % b))


