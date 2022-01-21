# TV 크기
d, h, w = map(int, input().split())
r = d / ((h**2 + w**2) ** 0.5)          # 대각선의 비율 : 대각선 길이 / 루트(세로비^2 + 가로비^2)
print(int(h * r), int (w * r))          # 각각 높이와 너비에 비율을 곱하고, int()를 통해 내림