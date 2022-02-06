# [기초-리스트] 이상한 출석 번호 부르기1
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)             (얘는 저장할 필요가 없어서 단순 입력만 받고 저장 안하고 구현함)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
attendance = [0 for i in range(23)]
int(input())
number_list = map(int, input().split())
for i in number_list:
    attendance[i - 1] += 1
for i in attendance:
    print(i, end=' ')