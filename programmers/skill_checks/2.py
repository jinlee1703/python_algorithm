def solution(answers):
    answer = []
    cnt = [0, 0, 0]

    one = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if one[i % len(one)] == answers[i]:
            cnt[0] += 1

        if two[i % len(two)] == answers[i]:
            cnt[1] += 1

        if three[i % len(three)] == answers[i]:
            cnt[2] += 1

    maxVal = max(cnt[0], cnt[1], cnt[2])

    for i in range(3):
        if maxVal == cnt[i]:
            answer.append(i + 1)

    return answer