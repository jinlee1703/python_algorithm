# [기초-종합] 빛 섞어 색 만들기
r, g, b = map(int, input().split())
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            # cnt += 1
# print(cnt)
print(r * g * b)    # 경우의 수는 서로 곱하여 구함