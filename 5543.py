# 상근날드
burger_list = []            # 버거들을 입력받을 리스트
for x in range(3):          # 버거 3개를 입력받아 저장
    burger_list.append(int(input()))

beverage_list = []          # 음료들을 입력받을 리스트
for x in range(2):          # 음료 2개를 입력받아 저장
    beverage_list.append(int(input()))

print(min(burger_list) + min(beverage_list) - 50)        # 가장싼 버거+음료 조합의 가격(세트는 -50원)을 출력