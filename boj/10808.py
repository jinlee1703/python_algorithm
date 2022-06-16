# 알파벳 개수
def alphabets_count(s):
    alphabets = [0 for _ in range(26)]
    for c in s:
        alphabets[ord(c)-97] += 1
    return str(alphabets).replace(',', '').replace('[', '').replace(']', '')


if __name__ == "__main__":
    s = input()
    print(alphabets_count(s))