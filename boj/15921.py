# 수찬은 마린보이야!!
n = int(input())
if n == 0:
    print("divide by zero")
else:
    li = list(map(int, input().split()))
    if len(li) == 0:
        print("divide by zero")
    else:
        ex = 0
        for i in li:
            ex += i * (1 / n)
        print('%.2f' % ((sum(li) / n) / ex))