# 별 찍기 - 12
n = int(input())
for i in range(1, n):
    print(' '*(n-i), end='')
    print('*'*i)
print('*'*n)
for i in range(n-1, 0, -1):
    print(' '*(n-i), end='')
    print('*'*i)