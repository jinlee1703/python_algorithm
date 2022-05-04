# 사탕 선생 고창영
t = int(input())
for _ in range(t):
    input()
    n = int(input())
    s = 0
    for __ in range(n):
        s += int(input())
    if s % n == 0:
        print("YES")
    else:
        print("NO")