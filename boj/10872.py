# 팩토리얼
def factorial(n):
    result = 1

    for x in range(1, n + 1):
        result *= x

    return result

print(factorial(int(input())))