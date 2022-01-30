# A+B - 8
T = int(input())
for x in range(1, T + 1):
    a, b = map(int, input().split())
    print("Case #%d: %d + %d = %d" % (x, a, b, a + b))