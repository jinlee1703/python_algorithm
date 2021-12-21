# 평균
n = int(input())                                    # 과목 개수
score_list = list(map(int, input().split()))        # 과목별 점수
sum = 0
for i in range(n):
    sum += score_list[i] / max(score_list) * 100
print(sum / n)