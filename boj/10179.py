# 쿠폰
t = int(input())
price = []
for i in range(t):
    n = float(input())
    price.append(n)
for i in price:
    print('$%.2f' % (i * 0.8))