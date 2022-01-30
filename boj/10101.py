# 삼각형 외우기
angle = [int(input()) for _ in range(3)]

# 세 각의 합이 180인 경우
if sum(angle) == 180:
    # 세 각의 크기가 모두 60이면, Equilateral
    if angle[0] == angle[1] == angle[2]:
        print("Equilateral")
    # 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
    elif angle[0] == angle[1] or angle[0] == angle[2] or angle[1] == angle[2]:
        print("Isosceles")
    # 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
    else:
        print("Scalene")
# 세 각의 합이 180이 아닌 경우에는 Error
else:
    print("Error")


# angle_list = []
# for x in range(3):
#     angle_list.append(int(input()))
#
# if angle_list[0] == angle_list[1] == angle_list[2] == 60:
#     # 세 각의 크기가 모두 60이면, Equilateral
#     print("Equilateral")
# elif sum(angle_list) == 180 and (angle_list[0] == angle_list[1] or angle_list[0] == angle_list[2] or angle_list[1] == angle_list[2]):
#     # 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
#     print("Isosceles")
# elif sum(angle_list) == 180 and not(angle_list[0] == angle_list[1] or angle_list[0] == angle_list[2] or angle_list[1] == angle_list[2]):
#     # 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
#     print("Scalene")
# elif sum(angle_list) != 180:
#     # 세 각의 합이 180이 아닌 경우에는 Error
#     print("Error")