# 별 찍기 - 6
n = int(input())
for i in range(n, 0, -1):
    print(" " * (n - i), end='')
    print("*" * (i * 2 - 1))