# 과목선택
subject1 = []
subject2 = []
for i in range(4):
    subject1.append(int(input()))
for i in range(2):
    subject2.append(int(input()))

subject1.sort(reverse=True)
subject2.sort(reverse=True)

sum = 0
for i in subject1[:3]:
    sum += i
sum += subject2[0]
print(sum)