import sys
from collections import deque

# 상, 우, 하, 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def check(i, j):
    visited[i][j] = 1
    que = deque()
    que.append((i,j))
    order = 0
    
    while que:
        x, y = que.popleft()

        if visited[x][y] == k:
            return y+1, x+1
        
        new_x = x + dx[order%4]
        new_y = y + dy[order%4]
        
        if new_x < 0 or new_x >= r or new_y < 0 or new_y >= c:
            order += 1
            que.append((x, y))
            continue
        
        if visited[new_x][new_y] == 0:
            que.append((new_x, new_y))
            visited[new_x][new_y] = visited[x][y] + 1
        else:
            order += 1
            que.append((x, y))
            
c, r = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
hall = [[0] * c for _ in range(r)]
visited = [[0] * c for _ in range(r)]

if c * r < k:
    print(0)
    exit(0)

print(*check(0, 0))