# [기초-리스트] 바둑알 십자 뒤집기
d = []      # 바둑판 리스트
# 기존의 바둑판 한줄씩 입력받기
for i in range(19):
    n = list(map(int, input().split()))
    d.append(n)

# 뒤집을 횟수 입력 받기
t = int(input())
for i in range(t) :
    # 기준으로 삼을 x, y좌표 입력받기
    x, y = map(int, input().split())
    for j in range(19) :
        d[j][y - 1] = int(not bool(d[j][y - 1]))        # 세로 줄 변경
        d[x - 1][j] = int(not bool(d[x - 1][j]))        # 가로 줄 변경

# 십자가 뒤집기 후 바둑판 출력
for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()