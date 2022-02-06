# [기초-리스트] 바둑판에 흰 돌 놓기
t = int(input())
baduk = [[0 for i in range(19)] for i in range(19)]
for i in range(t):
    x, y = map(int, input().split())
    baduk[x - 1][y - 1] = 1
for i in range(19):
    for j in range(19):
        print(baduk[i][j], end=' ')
    print()