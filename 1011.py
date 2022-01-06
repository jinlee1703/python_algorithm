# Fly me to the Alpha Centauri
# x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())        # x = 현재 위치, y = 목표 위치 (y > x)
    distance = y - x    # 이동해야 하는 거리
    n = 0

    while True:
        if distance <= n * (n + 1):
            break
        n += 1

    # 총 이동 거리가 n의 제곱보다 작거나 같을 때
    if distance <= n**2:
        print(n * 2 - 1)
    # 총 이동 거리가 n의 제곱보다 클 때
    else:
        print(n * 2)

# 참고 : https://eunhee-programming.tistory.com/99