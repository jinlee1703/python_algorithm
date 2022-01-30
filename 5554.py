# 심부름 가는 길
number_list = []
for i in range(4):
    number_list.append(int(input()))        # 걸리는 시간을 초단위로 입력받음

print(sum(number_list) // 60)               # 총 이동시간 x분
print(sum(number_list) % 60)                # 총 이동시간 y초