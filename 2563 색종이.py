main_paper = [[0 for _ in range(100)] for __ in range(100)]

paste_paper_size = 10
for i in range(int(input())):
    x, y = map(int, input().split())
    x -= 1; y -= 1

    for _y in range(10):
        main_paper[y+_y][x:x+10] = [1 for _ in range(10)]

area = 0
for line_y in main_paper:
    for line_x in line_y:
        if line_x:
            area += 1
print(area)