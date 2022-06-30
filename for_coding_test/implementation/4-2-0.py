def solution(n):
    h = 0
    m = 0
    s = 0
    result = 0

    while not (h == n and m == 59 and s == 59):
        if '3' in str(h) or '3' in str(m) or '3' in str(s):
            result += 1

        s += 1

        if s == 60:
            s = 0
            m += 1

        if m == 60:
            m = 0
            h += 1

    return result


if __name__ == "__main__":
    n = int(input())
    print(solution(n))