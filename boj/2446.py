# 별 찍기 - 9
n = int(input())
for i in range(0, n-1):
    print(' '*i, end='')
    print('*'*(n*2-1-i*2))
print(' '*(n-1), '*', sep='')
for i in range(n-2, -1, -1):
    print(' '*i, end='')
    print('*'*(n*2-1-i*2))