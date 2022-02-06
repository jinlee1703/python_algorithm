# 블랙잭
n, m = map(int, input().split())
c_list = list(map(int, input().split()))
s = 0
for i in c_list:
    for j in c_list:
        for k in c_list:
            if i != j and i != k and j != k and i + j + k > s and i + j + k <= m:
                s = i + j + k
print(s)