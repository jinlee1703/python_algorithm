# [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기
c = input()
for i in range(ord('a'), ord(c) + 1):
    print(chr(i), end=' ')