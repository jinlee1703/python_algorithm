# [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기
a, b = map(int, input().split())
# print(bool(a) == bool(b) == False)
print(not (bool(a) or bool(b)))
# 하나라도 True일 경우 or으로 인하여 True가 되면 결과적으로 not으로 인하여 False가 됨
# 둘다 False여야 not으로 인하여 True가 됨