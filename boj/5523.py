# 경기 결과
from sys import stdin
n = int(stdin.readline())
a_win = b_win = 0
for i in range(n):
    a, b = map(int, stdin.readline().split())
    if a > b:
        a_win += 1
    elif a < b:
        b_win += 1
print(a_win, b_win)