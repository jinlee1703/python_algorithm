# 소수 구하기
def isPrime(num):
    if num == 1:                    # 소수는 1 이상의, 1과 자기자신으로만 나누어 지는 자연수
        return False
    else:
        for i in range(2, int(num**0.5) + 1):       # 2 ~ 자기자신의 제곱근으로 나누어질 경우 : 소수가 아님을 반환
            if num % i == 0:
                return False
        return True

m, n = map(int, input().split())    # m < n

for i in range(m, n + 1):           # m과 n 사이의 소수 출력하기
    if isPrime(i):                  # 소수 여부를 체크
        print(i)                    # 소수 출력

# 참고 : https://deokkk9.tistory.com/17