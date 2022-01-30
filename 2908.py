# 상수
a, b = input().split()
a = int(a[::-1])        # [::-1]역순
b = int(b[::-1])

print(a) if a > b else print(b)     # 삼항 연산자