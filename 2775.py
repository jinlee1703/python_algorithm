# 부녀회장이 될테야
t = int(input())        # 테스트케이스 횟수

for _ in range(t):
    k = int(input())    # 층
    n = int(input())    # 호

    people = [i for i in range(1, n + 1)]   # 0층에서 1부터 n호까지의 각각 사람 수를 리스트에 담아둠

    for x in range(k):                      # 층만큼 반복(0에서 시작)
        for y in range(1, n):               # 호만큼 반복(1에서 시작)
            people[y] += people[y-1]        # 층이 바뀌면 i호에 사는 사람들도 늘어나는 것을 차근차근 바꿔준다
    print(people[-1])

# 참고 : https://yoonsang-it.tistory.com/12