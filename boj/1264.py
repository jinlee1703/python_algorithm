# 모음의 개수
array = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    input_data = input()

    if input_data == '#':
        break

    result = 0
    for i in array:
        result += input_data.count(i)

    print(result)