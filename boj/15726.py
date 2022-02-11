# 이칙연산
a, b, c = map(int, input().split())
li = []
li.append(int(a * b / c))
li.append(int(a / b * c))
print(max(li))