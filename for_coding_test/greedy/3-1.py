# 잔돈 동전 개수 구하기
# 화폐의 종류만큼 반복을 수행하기 때문에 화폐의 종류가 K개일 경우 시간복잡도 O(K)
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin      # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)