print("hihi")

print("hello")

def myFunc(v1, v2):
    global hap
    hap = v1 + v2
    return

hap = 0
num1 = 100
num2 = 200

myFunc(num1, num2)
print(hap)