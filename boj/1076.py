# 저항
res_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
result = 0
for i in range(3):
    s = input()
    if i == 0:
        result += res_list.index(s)*10
    elif i == 1:
        result += res_list.index(s)
    elif i == 2:
        result *= 10**res_list.index(s)
print(result)