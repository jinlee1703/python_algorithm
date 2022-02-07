# 분해합
n = int(input())
for i in range(1, n + 1):
    s = i + sum(map(int, str(i)))       # i를 문자열로 입력받아 한글자씩 더 함
    if s == n:
        print(i)
        exit(0)
print(0)