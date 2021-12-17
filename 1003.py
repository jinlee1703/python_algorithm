# 피보나치 함수
T = int(input())        # 테스트 케이스 개수

for tc in range(T):
    num = int(input())
    cnt_0 = [1, 0]  # 0의 호출 횟수를 기록하는 리스트
    cnt_1 = [0, 1]  # 1의 호출 횟수를 기록하는 리스트

    for i in range(2, num+1):
        cnt_0.append(cnt_0[i - 1] + cnt_0[i - 2])
        cnt_1.append(cnt_1[i - 1] + cnt_1[i - 2])

    print('{} {}'.format(cnt_0[num], cnt_1[num]))

# 참고 : https://jennnn.tistory.com/11