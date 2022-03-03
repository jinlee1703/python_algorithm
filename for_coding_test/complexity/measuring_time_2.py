# '선택 정렬'과 '파이썬의 기본 정렬 라이브러리'의 수행 시간(속도) 비교
# 선택 정렬의 최악의 시간 복잡도 O(N**2)
# 파이썬의 기본 정렬 라이브러리의 최악의 시간 복잡도O(NlogN) - 상대적으로 빠름

from random import randint
import time

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100))   # 1부터 100 사이의 랜덤한 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i       # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]     # 스와프

end_time = time.time()
print("선택 정렬 성능 측정:", end_time - start_time)    # 수행 시간 출력

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    array.append(randint(1, 100))   # 1부터 100 사이의 랜덤한 정수

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time()      # 측정 종료
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time)    # 수행 시간 출력

""" 
자신이 설계한 알고리즘의 성능을 실제로 확인하기 위해서, 시간 측정 라이브러리를 사용해보는 습관을 기르는 것이 좋다.
코딩 테스트에서 문제를 풀 때는 가독서응ㄹ 해치지 않는 선에서 최대한 복잡도가 낮게 프로그램을 작성해야 한다.
일반적으로 알고리즘 문제 풀이에서의 복잡도는 계산 복잡도를 의미하는 경우가 많으며, '소스코드가 복잡하게 생겼다'와는 다른 말로 사용된다는 점을 기억하자.
일반적으로 '복잡도'란 시간 복잡도를 의미
"""
