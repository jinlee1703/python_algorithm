# [기초-종합] 언제까지 더해야 할까?
# n = int(input())
# s = 0
# cnt = 0
# while True:
#     cnt += 1
#     if s + cnt < n:
#         s += cnt
#     else:
#         break
# print(cnt)

n = int(input())
s = 0
t = 0
while s < n:
    t += 1
    s += t
print(t)