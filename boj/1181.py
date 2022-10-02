# 단어 정렬

# 입력 받기
n = int(input())
arr = []
for _ in range(n):
    word = input()
    arr.append(word)

# 출력 시키기
arr = list(set(arr))
arr.sort()
arr.sort(key=len)
for w in arr:
    print(w)