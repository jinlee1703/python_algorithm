# 직사각형에서 탈출
x, y, w, h = map(int, input().split())  # 경계선에서 가장 가까운 값을 입력받기 위한 4가지의 값 출력
print(min(x, y, w-x, h-y))              # 최소값 출력

# if x > abs(x - w):
#     a = abs(x - w)
# else:
#     a = x
#
# if y > abs(y - h):
#     b = abs(y - h)
# else:
#     b = y
#
# if a > b:
#     print(b)
# else:
#     print(a)