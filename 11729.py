# 하노이 탑 이동 순서
# 하노이 탑 재귀 함수
def hanoi_tower(n, start, end):             # 
    if n == 1:
        print(start, end)
        return
    
    hanoi_tower(n-1, start, 6-start-end)    # 1단계 : n-1개의 원판을 1번 막대에서 2번 막대로 옮김
    print(start, end)                       # 2단계 : 남은 1개의 원판을 1번 막대에서 3번 막대로 옮김
    hanoi_tower(n-1, 6-start-end, end)      # 3단계 : 다시 n-1개의 원판을 2번 막대에서 3번 막대로 옮김

n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)

# 참고 : https://study-all-night.tistory.com/6