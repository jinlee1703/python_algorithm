# [기초-종합] 수 나열하기1 (등차수열)
# a : 시작값
# d : 등차
# n : 출력할 n번째 수
a, d, n = map(int, input().split())
print(a + d * (n - 1))