# 암호
plain_text = input()
key = input()
cyper_text = []
j = 0
for c in plain_text:
    if c == ' ':
        cyper_text.append(' ')
    else:
        i = ord(c) - (ord(key[j]) - 96)
        if i < 97:
            i += 26
        cyper_text.append(chr(i))

    j += 1
    if j == len(key):
        j = 0

for i in cyper_text:
    print(i, end='')