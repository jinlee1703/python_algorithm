# [기초-종합] 수 나열하기3
# a : 시작값
# m : 곱할 값
# d : 더할 값
# n : 출력할 n번째 수
a, m, d, n = map(int, input().split())
s = a
for i in range(n - 1):
    s = s * m + d
print(s)