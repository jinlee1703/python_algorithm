# 더하기 사이클
input_num = int(input())

num = input_num
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)                  # 10의 자리와 1의 자리를 더한 수
    new_num = ((num % 10) * 10) + (sum_num % 10)      # 기존 1의 자리를 10의 자리로 만들고 위의 수의 1의 자리를 더함
    cnt += 1
    if new_num == input_num:
        break
    num = new_num
print(cnt)

# 참고 : https://ooyoung.tistory.com/46