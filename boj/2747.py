# 피보나치 수
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 2) + fibonacci(n - 1)

n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = b, a + b
print(a)