# 알파벳 찾기
s = input()
alphabet = list(range(ord('a'), ord('z') + 1))
for x in alphabet:
    print(s.find(chr(x)), end=' ')

# for i in range(ord('a'), ord('z') + 1):
#     try:
#         print(s.index(chr(i)), end=' ')
#     except:
#         print(-1, end=' ')