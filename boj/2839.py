# 설탕 배달
n = int(input())
bag = 0
while n >= 0:
    if n % 5 == 0:          # 5의 배수이면
        bag += (n // 5)     # 5로 나눈 몫을 구해서 더해줌
        print(bag)
        break
    n -= 3                  # 5의 배수가 될 때까지 설탕-3, 봉지+1
    bag += 1
else:
    print(-1)

# 참고 : https://ooyoung.tistory.com/81