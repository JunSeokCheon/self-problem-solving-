import sys
from collections import deque

def bfs(i, j, depth, visited):
    que = deque()
    que.append([i,j])
    visited[i][j] = 1
    
    while que:
        x, y = que.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if visited[nx][ny] == 0:
                if board[nx][ny] > depth:
                    que.append([nx,ny])
                    visited[nx][ny] = 1
            
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
safe = 0
MAXNUM = 0

for i in range(N):
    for j in range(N):
        if board[i][j] >= MAXNUM:
            MAXNUM = board[i][j]

for depth in range(MAXNUM):
    visited = [[0]*N for _ in range(N)]
    compare_safe = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and board[i][j] > depth:
                bfs(i,j,depth, visited)
                compare_safe += 1
    
    safe = max(safe, compare_safe)
    
print(safe)