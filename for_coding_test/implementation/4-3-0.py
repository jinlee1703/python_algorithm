def solution(c):
    x_label = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    y_label = ['1', '2', '3', '4', '5', '6', '7', '8']

    dx = [2, 2, -2, -2, 1, -1, 1, -1]
    dy = [1, -1, 1, -1, 2, 2, -2, -2]

    x = x_label.index(c[0]) + 1
    y = y_label.index(c[1]) + 1

    result = 0

    for i in range(8):
        if x + dx[i] >= 1 and x + dx[i] <= 8 and y + dy[i] >= 1 and y + dy[i] <= 8:
            result += 1

    return result


if __name__ == "__main__":
    c = input()
    print(solution(c))