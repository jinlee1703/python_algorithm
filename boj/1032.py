# 명령 프롬프트
def solution():
    n = int(input())
    pattern = []
    for _ in range(n):
        file_name = input()

        if len(pattern) == 0:
            pattern = list(file_name)
        else:
            for i in range(len(file_name)):
                if pattern[i] != file_name[i]:
                    pattern[i] = '?'

    print(
        str(pattern)
            .replace('\'', '')
            .replace('[', '')
            .replace(']', '')
            .replace(', ', '')
    )


if __name__ == "__main__":
    solution()