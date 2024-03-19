points = []
for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))

x_coordinates = [point[0] for point in points]
y_coordinates = [point[1] for point in points]

for x in x_coordinates:
    if x_coordinates.count(x) == 1:
        fourth_x = x
        break

for y in y_coordinates:
    if y_coordinates.count(y) == 1:
        fourth_y = y
        break

print(fourth_x, fourth_y)
