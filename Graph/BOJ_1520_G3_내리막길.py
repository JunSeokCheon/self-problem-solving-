import sys
sys.setrecursionlimit(10 ** 8)

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]
    
    visited[x][y] = 0
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        
        if board[x][y] > board[nx][ny]:
            visited[x][y] += dfs(nx,ny)
    
    return visited[x][y]
    

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

m, n = map(int, sys.stdin.readline().split())
board = []
visited = [[-1]*n for _ in range(m)]

for _ in range(m):
    board.append(list(map(int, sys.stdin.readline().split())))

print(dfs(0,0))