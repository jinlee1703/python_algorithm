# 국회의원 선거
import sys

N = int(sys.stdin.readline().rstrip())

vote = list()  # 득표수
for i in range(0, N):
    vote.append(int(sys.stdin.readline().rstrip()))

answer = 0
m = max(vote)

while m != vote[0] or vote.count(m) >= 2:
    maxIndex = vote[1:].index(max(vote[1:])) + 1
    vote[0] += 1
    vote[maxIndex] -= 1
    answer += 1
    m = max(vote)

<<<<<<< HEAD
print(answer)
=======
print(answer)
>>>>>>> d0cb64bf16f8117280c393edd297895924af1029
