# 별 찍기 - 10
# 별을 찍는 재귀 함수
def draw_star(n):
    global Map                              # 메인 데이터 Map 리스트를 Global(전역변수) 사용

    if n == 3:                              # 사용자 입력값이 3일 경우
        Map[0][:3] = Map[2][:3] = [1]*3     # 첫번째 줄과 마지막 줄은 1로 채움
        Map[1][:3] = [1, 0, 1]              # 중간 줄은 1 0 1
        return
                                            # else
    a = n // 3                              # n / 3의 몫을 저장
    draw_star(n // 3)                       # n / 3을 인자로 재귀함수 호출
    for i in range(3):                      # 3행 * 3열 반복
        for j in range(3):
            if i == 1 and j == 1:           # 가운데일 경우 비워줌
                continue
            for k in range(a):              # 가운데가 아닐 경우
                Map[a * i + k][a * j:a * (j + 1)] = Map[k][:a]      # 핵심 아이디어

n = int(input())

# 메인 데이터 선언
Map = [[0 for i in range(n)] for i in range(n)]     # n * n 크기의 리스트를 만들고 0(False)으로 초기화

draw_star(n)        # 별을 그리는 재귀함수 호출

for i in Map:                           # 2중 for문을 통해 리스트의 원소가 1(True)일 경우 *, 0(False)일 경우 공백을 출력
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# 참고 : https://study-all-night.tistory.com/5