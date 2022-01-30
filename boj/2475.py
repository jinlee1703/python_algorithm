# 검증수
number_list = list(map(int, input().split()))       # 5개의 숫자를 입력받음
result = 0
for i in number_list:       # 각 숫자들의 제곱을 합함
    result += i**2
print(result % 10)          # 합에 10을 나눈 나머지가 검증수