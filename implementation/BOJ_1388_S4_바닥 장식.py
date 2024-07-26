import sys
from collections import deque

def check(i,j):
    visited[i][j] = 1
    que = deque()
    que.append((i,j))
    
    while que:
        x, y = que.popleft()
        
        if board[x][y] == '-':
            for k in [-1, 1]:
                new_y = y + k
                
                if new_y < 0 or new_y >= m:
                    continue
                
                if board[x][new_y] == '|':
                    continue
                
                if visited[x][new_y] == 0:
                    que.append((x, new_y))
                    visited[x][new_y] = 1     
        elif board[x][y] == '|':
            for k in [-1, 1]:
                new_x = x + k
                
                if new_x < 0 or new_x >= n:
                    continue
                
                if board[new_x][y] == '-':
                    continue
                
                if visited[new_x][y] == 0:
                    que.append((new_x, y))
                    visited[new_x][y] = 1
                
n, m = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            check(i,j)
            result += 1
print(result)