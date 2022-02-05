# [기초-산술연산] 정수 2개 입력받아 자동 계산하기
a, b = map(int, input().split())
print(a + b)                    # 합
print(a - b)                    # 차
print(a * b)                    # 곱
print(a // b)                   # 나눗셈 : 몫
print(a % b)                    # 나눗셈 : 나머지
print('%.2f' % (a / b))         # 나눗셈