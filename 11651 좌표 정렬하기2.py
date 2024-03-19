n = int(input())
coordinate_y = {
    # "y" : [x1, x2, x3...]
    # 1. 키 정렬
    # 2. 정렬된 키와 함께 x값 정렬해서 순서대로 출력
}

for _ in range(n):
    x, y = map(int, input().split())
    if y not in coordinate_y:
        coordinate_y[y] = []
    coordinate_y[y].append(x)

for y in sorted(coordinate_y):
    coordinate_y[y].sort()
    for x in coordinate_y[y]:
        print(x, y)