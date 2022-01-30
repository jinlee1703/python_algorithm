# 평균 점수
total = 0
for x in range(5):
    num = int(input())
    if num < 40:
        num = 40
    total += num
print(total//5)