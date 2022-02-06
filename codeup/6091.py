# [기초-종합] 함께 문제 푸는 날
a, b, c = map(int, input().split())
n = 1
while not(n % a == n % b == n % c == 0):
    n += 1
print(n)