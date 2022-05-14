# 계산기 프로그램
result = int(input())
while True:
    op = input()
    if op == '=':
        print(result)
        break
    else:
        n = int(input())
        if op == '+':
            result += n
        elif op == '-':
            result -= n
        elif op == '*':
            result *= n
        elif op == '/':
            result //= n