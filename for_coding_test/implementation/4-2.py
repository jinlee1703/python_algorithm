def solution(h):
    count = 0

    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                # 매 시각 안에 3이 포함되어 있다면 카운트 증가
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    return count



if __name__ == "__main__":
    # H를 입력받기
    h = int(input())
    print(solution(h))