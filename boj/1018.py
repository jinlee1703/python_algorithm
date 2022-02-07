# 체스판 다시 칠하기
# 입력값 받기
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())
repair = []

# 처리
for i in range(n - 7):                          # i, j : 최대 크기(모서리) 조절       ex) 9*9에서 움직여서 조사할 수 있는 경우의 수는 2*2 4개
    for j in range(m - 7):
        first_w = 0
        first_b = 0
        for k in range(i, i + 8):               # k, l : 8 x 8 체스판 설정
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:            # 행과 열의 인덱스의 합이 짝수인 경우와 홀수인 경우의 색이 다름
                    if board[k][l] != 'W':      # w로 시작하는지
                        first_w += 1
                    if board[k][l] != 'B':      # b로 시작하는지 판단하고
                        first_b += 1
                else:
                    if board[k][l] != 'B':      # b로 시작하는지 판단하고
                        first_w += 1
                    if board[k][l] != 'W':      # w로 시작하는지
                        first_b += 1
        repair.append(first_w)                  # 바꿔야할 블럭을 체크
        repair.append(first_b)
print(min(repair))