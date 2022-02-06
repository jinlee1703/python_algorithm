# [기초-리스트] 성실한 개미
a_map = []
for i in range(10):
    line = list(map(int, input().split()))
    a_map.append(line)

x = 1
y = 1

while True:
    a_map[y][x] = 9             # 지나간 곳 표시
    if a_map[y][x + 1] == 0 or a_map[y][x + 1] == 2:
        x += 1
    elif a_map[y + 1][x] == 0 or a_map[y + 1][x] == 2:
        y += 1
    else:
        break

    cnt = 0
    for i in range(10):
        if a_map[i].count(2) != 0:
            cnt += 1
    if cnt == 0:
        break

for i in range(10):
    for j in range(10):
        print(a_map[i][j], end=' ')
    print()