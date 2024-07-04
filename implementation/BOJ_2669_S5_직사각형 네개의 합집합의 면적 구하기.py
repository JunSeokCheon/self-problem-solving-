import sys

triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
board = [[0]*101 for _ in range(101)]
result = 0

for tri in triangle:
    x1, y1, x2, y2 = tri[0], tri[1], tri[2], tri[3]
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

for bd in board:
    result += sum(bd)

print(result)