dots = int(input())
min_pos = [10000, 10000]
max_pos = [-10000, -10000]

for i in range(dots):
    x, y = map(int, input().split())

    min_pos[0] = min(min_pos[0], x)
    min_pos[1] = min(min_pos[1], y)

    max_pos[0] = max(max_pos[0], x)
    max_pos[1] = max(max_pos[1], y)

w = max_pos[0] - min_pos[0]
h = max_pos[1] - min_pos[1]

print(w*h)