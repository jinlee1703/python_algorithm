# 골드바흐의 추측
sosu = [0 for i in range(10001)]
sosu[1] = 1

for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        sosu[j] = 1

t = int(input())

for i in range(t):
    n = int(input())
    b = n // 2
    for j in range(b, 1, -1):
        if sosu[n - j] == 0 and sosu[j] == 0:
            print(j, n - j)
            break

# 참고 : https://pacific-ocean.tistory.com/129