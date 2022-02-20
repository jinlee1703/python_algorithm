# Do Not Touch Anything
# 좌석의 세로 크기 R
# 좌석의 가로 크기 C
# 한 대의 CCTV가 수용할 수 있는 범위 N
import math

r, c, n = map(int, input().split())
print(math.ceil(r / n) * math.ceil(c / n))