# 덩치
t = int(input())
li = []
for i in range(t):
    x, y = map(int, input().split())
    li.append([x, y])
for i in range(t):
    rank = 1
    for j in range(t):
        if i != j:
            if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
                rank += 1
    print(rank, end=' ')