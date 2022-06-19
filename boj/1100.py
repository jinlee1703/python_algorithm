# 하얀 칸
def func():
    cnt = 0
    for i in range(8):
        line = list(input())
        for j in range(len(line)):
            if (i % 2 == 0 and line[j] == 'F' and j % 2 == 0) or (i % 2 == 1 and line[j] == 'F' and j % 2 == 1):
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()