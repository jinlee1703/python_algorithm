# 오븐 시계
h, m = map(int, input().split())
m += int(input())

if m >= 60:             # 분이 60분 이상일 경우 => 시간을 증가
    h += m // 60
    m %= 60

if h >= 24:             # 시간이 24시간 이상일 경우 => --24
    h %= 24

print(h, m)