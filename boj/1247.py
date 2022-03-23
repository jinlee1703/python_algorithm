# 부호
for i in range(3):
    n = int(input())
    s = 0
    for j in range(n):
        s += int(input())
        sign = '+' if s > 0 else '-' if s < 0 else '0'
    print(sign)