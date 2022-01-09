# 베르트랑 공준
def isPrime(num):
    if num == 1:                                # 소수는 1 이상의, 1과 자기자신으로만 나누어 지는 자연수
        return False

    for i in range(2, int(num**0.5) + 1):       # 2 ~ 자기자신의 제곱근으로 나누어질 경우 : 소수가 아님을 반환
        if num % i == 0:
            return False
    return True

number_list = list(range(2, 123456*2 + 1))      # 문제의 제한 범위 전체 리스트
sosu_list = []

for i in number_list:                           # 문제의 제한 범위에서 소수만 리스트에 추가
    if isPrime(i):
        sosu_list.append(i)

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0

    for i in sosu_list:         # 소수만 있는 리스트에서 [입력값 ~ 입력값 * 1] 사이의 소수만 카운트 
        if n < i <= n * 2:
            cnt += 1
    print(cnt)

# 참고 : https://velog.io/@iillyy/%EB%B0%B1%EC%A4%80-4948%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC