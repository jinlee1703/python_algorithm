# [기초-조건/선택실행구조] 월 입력받아 계절 출력하기
# n = int(input())
# if n in (12, 1, 2):
#     print("winter")
# elif n in (3, 4, 5):
#     print("spring")
# elif n in (6, 7, 8):
#     print("summer")
# elif n in (9, 10, 11):
#     print("fall")
n = int(input())
if n // 3 == 1:
    print("spring")
elif n // 3 == 2:
    print("summer")
elif n // 3 == 3:
    print("fall")
else:
    print("winter")