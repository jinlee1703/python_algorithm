# 다이얼
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
second = 0
for i in word:              # ex) U, N, U, C, I, C
    for j in dial:          # ex) 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'
        if i in j:          # j에 i가 포함되어 있으면 ex) 'ABC'에 'U'가 포함되어 있으면
            second += dial.index(j) + 3
print(second)