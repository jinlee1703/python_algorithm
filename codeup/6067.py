# [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기
n = int(input())
if n < 0:
    print("A" if n % 2 == 0 else "B")
else:
    print("C" if n % 2 == 0 else "D")