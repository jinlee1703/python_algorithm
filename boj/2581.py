# 소수
m = int(input())                    # 작은 수
n = int(input())                    # 큰 수
sosu_list = []                      # 소수를 저장할 리스트
for x in range(m, n + 1):
    check = 0                       # 소수 여부를 체크할 변수
    if x > 1:                       # 수가 1보다 클 경우(1은 소수가 아니기 때문)
        for i in range(2, x):       # 2 ~ 입력한수-1 반복
            if x % i == 0:          # 나누어 떨어질 경우 -> 소수가 아님
                check = 1
                break

        if check == 0:              # 소수일 경우 -> 리스트에 추가
            sosu_list.append(x)

if len(sosu_list) > 0:              # 리스트의 크기가 0보다 클 경우(리스트에 소수가 있을 경우)
    print(sum(sosu_list))           # 소수의 합계 출력
    print(min(sosu_list))           # 가장 작은 소수 출력
else:
    print(-1)