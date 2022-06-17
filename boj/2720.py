# 세탁소 사장 동혁
def func():
    t = int(input())
    for i in range(t):
        c = int(input())
        q = c // 25
        c %= 25
        d = c // 10
        c %= 10
        n = c // 5
        c %= 5
        print(q, d, n, c)

if __name__ == "__main__":
    func()