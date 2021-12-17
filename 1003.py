# 피보나치 함수

def fibonacci(n):
    if n == 0:
        fibonacci.cnt_0 += 1
        return 0
    elif n == 1:
        fibonacci.cnt_1 += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

T = int(input())        # 테스트 케이스 개수

for i in range(T):
    num = int(input())
    fibonacci(num)
    # print('%d %d' % (cnt_0, cnt_1))