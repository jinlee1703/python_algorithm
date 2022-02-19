# 공백 없는 A+B
n = input()
if len(n) == 4:
    a = b = 10
elif len(n) == 2:
    a = int(n) // 10
    b = int(n) % 10
else:
    if int(n[2]) == 0:
        a = int(n) // 100
        b = 10
    else:
        a = 10
        b = int(n) % 10
print(a + b)