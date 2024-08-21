import sys
from collections import deque

def bfs(i, j):
    result = 0
    que = deque()
    que.append([i, j])
    visited[i][j] = 1
    
    while que:
        x, y = que.popleft()
        
        if campus[x][y] == 'P':
            result += 1
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if visited[nx][ny] == 0:
                if campus[nx][ny] == 'O' or campus[nx][ny] == 'P':
                    que.append([nx, ny])
                    visited[nx][ny] = 1
    
    return result

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
campus = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            doyeon_x, doyeon_y = i, j

result = bfs(doyeon_x, doyeon_y)
if result == 0:
    print('TT')
else:
    print(result)