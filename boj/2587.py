# 대표값2
arr = []

for _ in range(5):
    arr.append(int(input()))

print("%d" %(sum(arr)/5))
arr.sort()
print(arr[2])