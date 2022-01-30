# 파티가 끝나고 난 뒤
l, p = map(int, input().split())            # l = 1m제곱당 사람의 수, p = 파티가 열렸던 곳의 넓이
number_list = map(int, input().split())     # 각 기사에 실려있는 참가자의 수

ex = l * p                                  # 상근이가 계산한 참가자의 수
for i in number_list:                       # 각 기사에 실려있는 참가자와 상근이가 계산한 참가자 수를 비교하여 출력
    print(i - ex, end=' ')