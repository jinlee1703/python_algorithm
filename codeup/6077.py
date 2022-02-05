# [기초-종합] 짝수 합 구하기
s = 0
for x in range(1, int(input()) + 1):
    if x % 2 == 0:
        s += x
print(s)