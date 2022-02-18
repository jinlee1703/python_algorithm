# 팀 나누기
li = list(map(int, input().split()))
li.sort()
team_1 = li[0] + li[3]
team_2 = li[1] + li[2]
print(abs(team_1 - team_2))