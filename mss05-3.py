import random

a = random.randrange(1, 8)

if a == 1:
    print("도")
elif a == 2:
    print("개")
elif a == 3:
    print("걸")
elif a == 4:
    print("윷")
elif a == 5:
    print("모")
elif a == 6:
    print("빽도")
else:
    print("조커...?")

# switch
def switch(i):
    return {1: "도", 2: "개", 3: "걸", 4: "윷",5: "모",6: "빽도", 7: "조커"}.get(i)


print(switch(a))