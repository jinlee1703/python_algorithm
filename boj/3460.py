# 이진수
t = int(input())
for _ in range(t):
    n = bin(int(input()))
    arr = list(n[2:])
    arr.reverse()
    for i in range(len(arr)):
        if arr[i] == '1':
            print(i, end=' ')
    print()