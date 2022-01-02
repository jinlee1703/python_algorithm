# 달팽이는 올라가고 싶다
import math

# a = 낮에 올라간 거리, b = 밤에 미끄러진 거리, v = 나무 막대의 높이
a, b, v = map(int, input().split())

#  나무 높이 v에서 정상에 도달 후 미끄러지지 않는 b를 빼면 매일 (a-b)만큼씩 올라가게 된다.
# 수식을 정리하면, 달팽이는 (v-b) / (a-b)일 동안 올라가게 된다.
# 마지막 날은 조금만 올라도 하루가 지난 것으로 치니 소숫점이 나오게 되면 ceil로 올림 처리해 하루를 더 세준다.
crawl = math.ceil((v - b) / (a - b))
print(crawl)

# 참고 : https://velog.io/@junyp1/%EB%B0%B1%EC%A4%80-2869-Python-%EB%8B%AC%ED%8C%BD%EC%9D%B4%EB%8A%94-%EC%98%AC%EB%9D%BC%EA%B0%80%EA%B3%A0-%EC%8B%B6%EB%8B%A4-bf88uea8