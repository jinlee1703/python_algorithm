# [기초-리스트] 이상한 출석 번호 부르기2
t = int(input())
number_list = list(map(int, input().split()))
for i in range(t - 1, -1, -1):          # 9 ~ 0, -1 감소
    print(number_list[i], end=' ')