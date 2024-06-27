import sys
from collections import deque

# 동, 서, 남, 북 
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

que = deque()
que.append([0,0])

while que:
    x, y = que.popleft()
    
    if x == n-1 and y == m-1:
        print(miro[n-1][m-1])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if miro[nx][ny] == 1:
            que.append([nx,ny])
            miro[nx][ny] = miro[x][y] + 1