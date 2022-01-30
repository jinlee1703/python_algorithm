# 크로아티아 알파벳
c_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()
for i in c_alphabets:               # 알파벳 하나 씩 반복
    str = str.replace(i, '*')       # 해당하는 알파벳이 있으면 '*'로 바꿈으로써 문자 한개로 만듦
print(len(str))                     # 입력받은 문자열의 글자 수(크로아티아 알파벳은 문자 1개임)를 출력