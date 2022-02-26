# 전자레인지
# 첫 줄에는 원래의 고기의 온도 A가 주어진다. 단, A는 -100 이상 100 이하이며, 0이 아니다.
# 둘째 줄에는 목표 온도 B가 주어진다. 단, B는 1 이상 100 이하이며, A보다 크다.
# 셋째 줄에는 얼어 있는 고기를 1℃ 데우는 데 걸리는 시간 C가 주어진다.
# 넷째 줄에는 얼어 있는 고기를 해동하는 데 걸리는 시간 D가 주어진다.
# 다섯째 줄에는 얼어 있지 않은 고기를 1℃ 데우는 데 걸리는 시간 E가 주어진다.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

t = 0
ice = True

while a != b:
    if a < 0:
        t += c
        a += 1
    elif a == 0 and ice:
        t += d
        ice = False
    else:
        t += e
        a += 1
print(t)