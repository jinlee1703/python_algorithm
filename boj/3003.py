# 킹, 퀸, 룩, 비숍, 나이트, 폰
chess_list = [1, 1, 2, 2, 2, 8]                 # 체스에 필요한 말의 개수
own_list = list(map(int, input().split()))      # 보유하고 있는 말의 개수

for x in range(len(chess_list)):                # 필요한 말의 개수 - 보유한 말의 개수를 출력
    print(chess_list[x] - own_list[x], end=' ')