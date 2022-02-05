# [기초-종합] 3 6 9 게임의 왕이 되자
n = int(input())
for i in range(1, n + 1):
    c = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if c != 0:
        print('X' * c, end=' ')
    else:
        print(i, end=' ')

# 홈페이지에 있는 풀이, 조건으로 n <= 30이었기 때문에 문제가 없지만 33부터는 XX로 출력해야하는데 이 경우 올바르게 출력될 수 없음
# 위의 코드보단 코드길이가 짧음
# n = int(input())
# for i in range(1, n + 1):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         print('X', end=' ')
#     else:
#         print(i, end=' ')