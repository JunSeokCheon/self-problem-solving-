import sys, heapq

def dijkstra(x, y):
    que = []
    heapq.heappush(que, (0, x, y))
    distance[x][y] = 0
    
    while que:
        dist, a, b = heapq.heappop(que)
        
        if dist > distance[a][b]:
            continue
        
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if dist + 1 < distance[nx][ny]:
                if board[nx][ny] == 1:
                    distance[nx][ny] = min(dist, distance[nx][ny])
                    heapq.heappush(que, (dist, nx, ny))
                else:
                    distance[nx][ny] = min(dist + 1, distance[nx][ny])
                    heapq.heappush(que, (dist+1, nx, ny))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
distance = [[1e9]*(n) for _ in range(n)]

dijkstra(0,0)
print(distance[n-1][n-1])