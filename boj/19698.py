# 헛간 청약
n, w, h, l = map(int, input().split())
a = w // l
b = h // l
if n > a * b:
    print(a*b)
else:
    print(n)