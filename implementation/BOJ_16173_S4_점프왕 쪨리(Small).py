import sys
from collections import deque

def bfs(x, y):
    que = deque()
    que.append((x, y))
    
    while que:
        a, b = que.popleft()
        temp_value = map[a][b]
        
        if map[a][b] == -1:
            return True
        
        for k in range(2):
            nx = a + dx[k] * temp_value
            ny = b + dy[k] * temp_value
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                que.append((nx, ny))
    return False

N = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 1]
dy = [1, 0]

visited = [[0]*N for _ in range(N)]

if bfs(0,0):
    print('HaruHaru')
else:
    print('Hing')