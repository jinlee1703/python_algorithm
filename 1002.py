# 터렛
T = int(input())        # 테스트 케이스의 개수

for i in range(0, T):
    str = input()
    arr = str.split(' ')

    point1 = arr[0], arr[1]
    r1 = arr[2]

    point2 = arr[3], arr[4]
    r2 = arr[5]

# 풀이 : https://eine.tistory.com/entry/%EB%B0%B1%EC%A4%80%EC%A0%80%EC%A7%80-1002%EB%B2%88-%ED%84%B0%EB%A0%9B-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4