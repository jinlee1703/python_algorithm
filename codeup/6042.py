# [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기
f = float(input())
# print(round(f, 2))        # 반올림
print('%.2f' % f)           # 2자리수만 출력