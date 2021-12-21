# 나머지
number_set = set([])
for i in range(10):
    n = int(input())
    number_set.add(n%42)

print(len(number_set))