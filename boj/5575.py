# 타임 카드
for i in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())              # s~ : 출근 시/분/초, e~ : 퇴근 시/분/초
    t = (eh * 3600 + em * 60 + es) - (sh * 3600 + sm * 60 + ss)     # 총 업무시간을 초단위로 계산
    print(t // 3600, t % 3600 // 60, t % 3600 % 60)                 # 시, 분, 초로 출력