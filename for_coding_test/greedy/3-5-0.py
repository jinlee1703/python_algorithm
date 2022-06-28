def solution(n, k):
    count = 0
    while not(n == 1):
        if n % k == 0:
            n //= k
        else:
            n -= 1
        count += 1
    return count

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solution(n, k))