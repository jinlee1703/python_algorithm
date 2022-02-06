# [기초-종합] 거기까지! 이제 그만~
n = int(input())
sum = 0
for i in range(1, n + 1):
    if sum >= n:
        break
    sum += i
print(sum)