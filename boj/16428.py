# A/B - 3
a, b = map(int, input().split())
c, d = divmod(a, b)     # divmod : 정수1을 2로나눈 몫과 나머지가 튜플 형태로 반환
if a != 0 and d < 0:    # 나누려는 값이 0이 아니고 나누는 값이 음수일 경우
    c, d = c+1, d-b     # 몫++, 나머지-나누려는값
print(c, d, sep='\n')