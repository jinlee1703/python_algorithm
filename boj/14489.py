# 치킨 두 마리 (...)
a, b = map(int, input().split())
price = int(input()) * 2
result = a + b - price
print(result if result > 0 else result + price)