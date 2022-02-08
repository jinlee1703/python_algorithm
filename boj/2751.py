# 수 정렬하기 2
t = int(input())
number_list = []

for i in range(t):                      # 입력
    number_list.append(int(input()))

for i in sorted(number_list):           # 정렬된 list 출력
    print(i)

# Python 제출 : 시간초과 / PyPy 제출 : 성공
# 참고 : https://assaeunji.github.io/python/2020-05-06-bj2751/