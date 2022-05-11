# 짝수를 찾아라
t = int(input())
for _ in range(t):
    arr = map(int, input().split())
    sum = 0
    min = 100
    for i in arr:
        if i % 2 == 0:
            sum += i
            if min > i:
                min = i
    print(sum, min)