# 수학은 체육과목 입니다 2
n = int(input())
n %= 8
print((10 - n) % 8 if n > 5 or n == 0 else n)