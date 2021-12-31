# 벌집
n = int(input())                # 방 번호 n
check = 1                       # 라인별 방 갯수
count = 1                       # 라인
while n > check:                # 방 번호 > 방 갯수 (방 찾기)
    count += 1                  # 다음 라인
    check += (count - 1) * 6    # 라인별 방 갯수 변경
print(count)                    # 라인 출력

# 참고 : https://pacific-ocean.tistory.com/102