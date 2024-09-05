import sys
from collections import deque

def bfs(board, i, j):
    result = 1
    # que = deque()
    # que.append([i, j, board[i][j]])
    que = set([(i, j, board[i][j])])
    while que:
        x, y, alpha = que.pop()
        result = max(result, len(alpha))
        print(alpha)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            
            if board[nx][ny] not in alpha:
                que.add((nx, ny, alpha+board[nx][ny]))
    
    return result
    

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

r, c = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

print(bfs(board, 0, 0))
