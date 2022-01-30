# 평균은 넘겠지
c = int(input())

for i in range(c):
    stu = list(map(int, input().split()))
    average = sum(stu[1:]) / stu[0]
    cnt = 0
    for j in stu[1:]:
        if j > average:
            cnt += 1
    print("%.3f%%" % (cnt/stu[0]*100))