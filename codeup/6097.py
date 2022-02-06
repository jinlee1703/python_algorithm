# [기초-리스트] 설탕과자 뽑기
# 입력
h, w = map(int, input().split())
panel = [[0 for i in range(w)] for i in range(h)]
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            panel[x - 1][y - 1 + j] = int(not bool(panel[x - 1][y - 1 + j]))
        else:
            panel[x - 1 + j][y - 1] = int(not bool(panel[x - 1 + j][y - 1]))

# 출력
for i in range(h):
    for j in range(w):
        print(panel[i][j], end=' ')
    print()