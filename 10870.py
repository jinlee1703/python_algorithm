# 피보나치 수 5
# 재귀 함수를 사용한 코드
def fibonacci(num):
    if num < 2:         # 0번째, 1번째 원소일 경우 0, 1 추가
        return num
    else:               # i-2번째 원소와 i-1번째 원소의 합을 추가
        return fibonacci(num - 2) + fibonacci(num - 1)

n = int(input())
print(fibonacci(n))


# 재귀 함수를 사용하지 않은 코드
# fibonacci_list = []
# n = int(input())
#
# for i in range(n + 1):
#     if i < 2:
#         fibonacci_list.append(i)
#     else:                           # i-2번째 원소와 i-1번째 원소의 합을 추가
#         fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])
#
# print(fibonacci_list[n])