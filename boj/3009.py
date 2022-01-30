# 네 번째 점
xList = []      # 3개의 점의 각각 x와 y 좌표를 입력받을 리스트
yList = []

for i in range(3):                          # 3개의 점 입력 받기
    x, y = map(int, input().split())        # 각 점의 x, y값을 변수에 저장
    xList.append(x)                         # x좌표와 y좌표를 각 리스트에 추가
    yList.append(y)

for i in range(3):                          # 3개의 점을 반복문을 통해 확인
    if xList.count(xList[i]) == 1:          # 리스트의 i번째 x좌표의 개수가 1개일 경우(2개여야 정사각형이 됨)
        x = xList[i]                        # x를 리스트에서 개수가 1개인 x좌표로 설정
    if yList.count(yList[i]) == 1:          # 리스트의 i번째 y좌표의 개수가 1개일 경우(2개여야 정사각형이 됨)
        y = yList[i]                        # y를 리스트에서 개수가 1개인 y좌표로 설정

print(x, y)