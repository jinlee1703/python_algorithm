# [기초-종합] 수 나열하기2 (등비수열)
# a : 시작값
# r : 등비
# n : 출력할 n번째 수
a, r, n = map(int, input().split())
s = a
for i in range(n - 1):
    s *= r
print(s)