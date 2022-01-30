# 그룹 단어 체커
n = int(input())
result = n
for i in range(n):                      # 테스트 케이스 만큼 반복
    word = input()                      # 단어 입력 받기
    for j in range(len(word) - 1):      # 단어[0:마지막글자-1]까지 반복
        if word[j] == word[j + 1]:      # 단어[j번째 원소] == 단어[j+1 원소]가 같으면
            pass                        # 생략
        elif word[j] in word[j + 1:]:   # 단어[j번째 원소]가 단어[j+1 원소:끝]에 포함되어 있으면
            result -= 1                 # 단어의 총 개수-=1
            break                       # 반복문 j 종료 -> 다음 단어 입력 받기
print(result)                           # 그룹 단어 개수 출력