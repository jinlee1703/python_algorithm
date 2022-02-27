# 카드 뽑기
n, m, k = map(int, input().split())
print(min(m, k) + n - max(m, k))        # 둘 중 작은 것 + 둘 중 큰 것