import sys
from collections import deque

def bfs(start_x, start_y):
    que = deque()
    que.append([start_x, start_y])
    visited[start_x][start_y] = 1
    
    while que:
        x, y = que.popleft()
        
        if x == goal_x and y == goal_y:
            return visited[x][y] -1
        
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            
            if visited[nx][ny] == 0:
                que.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1
                

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

T = int(sys.stdin.readline())

for _ in range(T):
    l = int(sys.stdin.readline())
    start_x, start_y = map(int, sys.stdin.readline().split())
    goal_x, goal_y = map(int, sys.stdin.readline().split())
    visited = [[0]*(l+1) for _ in range(l+1)]
    print(bfs(start_x, start_y))