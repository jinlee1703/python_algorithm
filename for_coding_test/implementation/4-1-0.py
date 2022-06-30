def solution(n, a):
    xy = [1, 1]
    arr = a.split()
    for i in arr:
        if i == 'L' and xy[0] != 1:
            xy[0] -= 1
        elif i == 'R' and xy[0] != 5:
            xy[0] += 1
        elif i == 'U' and xy[1] != 1:
            xy[1] -= 1
        elif i == 'D' and xy[1] != 5:
            xy[1] += 1
    return str(xy[1]) + " " + str(xy[0])


if __name__ == "__main__":
    n = int(input())
    a = input()
    print(solution(n, a))