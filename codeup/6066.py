# [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기
a, b, c = map(int, input().split())
print("even" if a % 2 == 0 else "odd")
print("even" if b % 2 == 0 else "odd")
print("even" if c % 2 == 0 else "odd")