sticks = sorted(list(map(int, input().split())))
if sticks[0] + sticks[1] > sticks[2]:
    print(sum(sticks))
else:
    print((sticks[0] + sticks[1]) * 2 - 1)