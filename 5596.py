# 시험 점수
minkuk_list = list(map(int, input().split()))
mansei_list = list(map(int, input().split()))

print(max(sum(minkuk_list), sum(mansei_list)))      # 민국의 시험 점수 합과 만세의 시험 점수 합을 비교하여 더 큰 수를 출력