# 수도요금
# X사 : 1리터당 A엔
# Y사 : 기본요금은 B엔
# P : JOI군의 집에서 한 달간 쓰는 수도의 양
# 사용량이 C리터 이하라면 요금은 기본요금만 청구된다
# 사용량이 C리터가 넘었을 경우 기본요금 B엔에 더해서 추가요금이 붙는다
# 추가요금은 사용량이 C리터를 넘었을 경우 1리터를 넘었을 때마다 D엔이다.
A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

x = A * P
y = B if P <= C else B + (P - C) * D
print(min(x, y))