# 최소, 최대
n = int(input())
number_list = list(map(int, input().split()))

print(min(number_list), max(number_list))

# max = number_list[0]
# min = number_list[0]
# for i in number_list[1:]:
#     if max < i:
#         max = i
#     if min > i:
#         min = i
# print(min, max)