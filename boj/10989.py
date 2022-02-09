# 수 정렬하기 3
import sys

n = int(sys.stdin.readline())
number_list = [0] * 10001                               # 10000개 원소를 가지는 리스트 생성

for i in range(n):
    number_list[int(sys.stdin.readline())] += 1         # n번째 원소++ : n=7일 경우 7이 1개 입력되었다는 뜻

for i in range(10001):                                  # 원소들을 for 반복문으로 점검
    if number_list[i] != 0:                             # i번째 원소가 0이 아닐경우(입력된 적이 있는 수일 경우)
        for j in range(number_list[i]):                 # i번째 원소를 ++한만큼(입력된 횟수만큼) 출력
            print(i)

# 참고 : https://yoonsang-it.tistory.com/49