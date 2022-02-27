# 나이 계산하기
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
o1 = 0
if m1 < m2:
    o1 = y2-y1
elif m1 == m2:
    if d1 <= d2:
        o1 = y2 - y1
    else:
        o1 = y2 - y1 - 1
else:
    o1 = y2 - y1 - 1
o2 = y2 - y1 + 1
o3 = y2 - y1
print(o1, o2, o3, sep='\n')