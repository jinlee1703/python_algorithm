# 직각삼각형
# 공식 참고 : https://mathbang.net/132
while(True):
    leg_list = list(map(int, input().split()))

    if leg_list.count(0) == 3:      # 0을 3개 입력했을 경우 종료
        break

    leg_list.sort()                 # 작은 순서대로 정렬

    if leg_list[0]**2 + leg_list[1]**2 == leg_list[2]**2:       # 직각삼각형 여부 공식 : [변1^2] + [변2^2] = [제일큰변^2]
        print("right")
    else:
        print("wrong")