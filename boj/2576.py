# 홀수
arr = []
for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        arr.append(n)
if len(arr) != 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)