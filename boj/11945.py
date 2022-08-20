# 뜨거운 붕어빵
n, m = map(int, input().split())
for i in range(n):
    line = list(input())
    line.reverse()
    print(''.join(str(s) for s in line))