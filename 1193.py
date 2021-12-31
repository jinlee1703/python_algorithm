# 분수찾기
x = int(input())
line = 0                # 사선 라인
max_num = 0             # 입력된 x의 라인에서 가장 큰 숫자
while x > max_num:
    line += 1
    max_num += line

gap = max_num - x
if line % 2 == 0:       # 사선 라인이 짝수일 때
    top = line - gap    #   분자
    under = gap + 1     #   분모
else:                   # 사선 라인이 홀수일 때
    top = gap + 1       #   분자
    under = line - gap  #   분모
print("%d/%d" %(top, under))

# 참고 : https://ooyoung.tistory.com/84