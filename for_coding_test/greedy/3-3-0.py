def solution():
    n, m = map(int, input().split())
    cards = []
    card = 0
    for i in range(n):
        cards.append(list(map(int, input().split())))
    for i in range(n):
        if card < min(cards[i]):
            card = min(cards[i])
    print(card)


if __name__ == "__main__":
    solution()