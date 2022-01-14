# 수 정렬하기
n = int(input())
number_list = []
for i in range(n):
    number_list.append(int(input()))

number_list.sort()

for i in number_list:
    print(i)

# 버블정렬, 삽입정렬 : https://0ver-grow.tistory.com/412