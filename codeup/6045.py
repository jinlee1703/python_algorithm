# [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
number_list = list(map(int, input().split()))
print('%d %.2f' % (sum(number_list), sum(number_list) / 3))