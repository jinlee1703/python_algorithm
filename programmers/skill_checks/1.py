import math

def solution(n):
    answer = 0
    result = math.sqrt(n)
    if result % 1 == 0:
        answer = (result+1)**2
    else:
        answer = -1
    return answer