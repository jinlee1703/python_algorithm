# 문자열 반복
t = int(input())
for x in range(t):
    r, s = input().split()
    str = ''
    for i in s:
        str += i*int(r)
    print(str)