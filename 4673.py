# 셀프 넘버
number_set = set(range(1, 10001))

for i in range(1, 10001):
    sum = i
    for j in str(i):
        sum += int(j)
    try:
        number_set.remove(sum)
    except:
        pass
for i in number_set:
    print(i)

# 다른 방법 : https://wook-2124.tistory.com/252