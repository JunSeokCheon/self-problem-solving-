import sys
from collections import deque

dx = [-1, 0, 1, 0, 1, -1, 1, -1]
dy = [0, -1, 0, 1, 1, -1, -1, 1]

def bfs(i, j, visited):
    que = deque()
    que.append(([i,j]))
    visited[i][j] = 1
    
    while que:
        x, y = que.popleft()
        
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            
            if visited[nx][ny] == 0:
                if board[nx][ny] == 1:
                    que.append([nx,ny])
                    visited[nx][ny] = 1
                
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    count = 0
    
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and board[i][j] == 1:
                bfs(i, j, visited)
                count += 1
    
    print(count)