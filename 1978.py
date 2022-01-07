# 소수 찾기
# 소수는 1보다 큰, 1과 자기 자신 이외의 수로 나누어 지지 않는 자연수
n = int(input())
number_list = list(map(int, input().split()))
cnt = 0

for x in number_list:
    check = 0
    if x != 1:
        for i in range(2, x):
            if x % i == 0:
                check = 1
        if check == 0:
            cnt += 1
print(cnt)