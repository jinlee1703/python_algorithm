# 벌집
n = int(input())                # 방 번호 n
check = 1                       #
count = 1
while n > check:
    count += 1
    check += (count - 1) * 6
print(count)

# 참고 : https://pacific-ocean.tistory.com/102