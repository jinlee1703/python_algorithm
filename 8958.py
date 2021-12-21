# OX퀴즈
n = int(input())
for i in range(n):
    str_list = list(input())
    cnt = 1
    score = 0
    for j in str_list:
        if j == 'O':
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)