# 주사위 세개
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a * 1000)
elif a == b:
    print(1000 + a * 100)
elif a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)

# dice_list = list(map(int, input().split()))
# cnt_list = []
# result = 0
#
# cnt_list.append(dice_list.count(dice_list[0]))
# cnt_list.append(dice_list.count(dice_list[1]))
# cnt_list.append(dice_list.count(dice_list[2]))
#
# if max(cnt_list) == 3:
#     result = 10000 + dice_list[cnt_list.index(max(cnt_list))] * 1000
# elif max(cnt_list) == 2:
#     result = 1000 + dice_list[cnt_list.index(max(cnt_list))] * 100
# elif max(cnt_list) == 1:
#     result = max(dice_list) * 100
# print(result)