# 치킨 두 마리 (...)
a, b = map(int, input().split())
price = int(input())
ownMoney = a + b
chickenTwoPrice = price * 2
print(ownMoney - chickenTwoPrice if ownMoney >= chickenTwoPrice else ownMoney)