# Counting Sort

input()

cards = {}

for card in list(input().split()):
    if card not in cards:
        cards[card] = 1
    else:
        cards[card] += 1

input()

for check in list(input().split()):
    if check in cards:
        print(cards[check], end=" ")
    else:
        print(0, end=" ")