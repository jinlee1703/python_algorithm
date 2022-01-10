# 골드바흐의 추측
sosu = [0 for i in range(10001)]                        # 원소의 개수가 100000개인 리스트를 생성하고 0으로 초기화
sosu[1] = 1                                             # 1번째 원소를 1(소수가 아님)로 설정

for i in range(2, 98):                                  # 2 ~ 97 반복
    for j in range(i * 2, 10001, i):                    # '에라토스테네스의 체'를 통해 소수가 아닌 수를 1로 설정
        sosu[j] = 1                                     # https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4

print(sosu)


# t = int(input())                                        # 테스트 케이스 입력
#
# for i in range(t):                                      # 테스트 케이스 횟수만큼 반복
#     n = int(input())                                    # 골드바흐 파티션을 출력하기 위한 숫자 입력받기
#     b = n // 2                                          # 입력받은 숫자를 2로 나눈 몫만 저장
#     for j in range(b, 1, -1):                           # 입력받은 숫자를 2로 나눈 몫 ~ 1까지 역순으로 반복
#         if sosu[n - j] == 0 and sosu[j] == 0:           # 입력받은 수-(입력받은 수//2 ~ 1)는 소수 && (입력받은 수//2 ~ 1)는 소수 == 골드바흐 파티션
#             print(j, n - j)                             # 골드바흐 파티션 출력
#             break

# 참고 : https://pacific-ocean.tistory.com/129