n = int(input())
coordinate_x = {
    # "x" : [y1, y2, y3...]
    # 1. 키 정렬
    # 2. 정렬된 키와 함께 y값 정렬해서 순서대로 출력
}

for _ in range(n):
    x, y = map(int, input().split())
    if x not in coordinate_x:
        coordinate_x[x] = []
    coordinate_x[x].append(y)

for x in sorted(coordinate_x):
    coordinate_x[x].sort()
    for y in coordinate_x[x]:
        print(x, y)