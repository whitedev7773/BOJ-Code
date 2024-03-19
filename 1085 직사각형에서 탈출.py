x, y, w, h = map(int, input().split())

horizontal_distance = min(x, w - x)
vertical_distance = min(y, h - y)

print(min(horizontal_distance, vertical_distance))