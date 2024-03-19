N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(input())

min_repaint = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        repaint_count_1 = 0
        repaint_count_2 = 0
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    if board[i + x][j + y] != 'W':
                        repaint_count_1 += 1
                    if board[i + x][j + y] != 'B':
                        repaint_count_2 += 1
                else:
                    if board[i + x][j + y] != 'B':
                        repaint_count_1 += 1
                    if board[i + x][j + y] != 'W':
                        repaint_count_2 += 1
        min_repaint = min(min_repaint, repaint_count_1, repaint_count_2)

print(min_repaint)
