# 농구 경기
n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
str = ""
for i in range(ord('a'), ord('z') + 1):
    cnt = 0
    for j in arr:
        if j.find(chr(i)) == 0:
            cnt += 1
            if cnt == 5:
                str += chr(i)
                break
if str == "":
    print("PREDAJA")
else:
    print(str)