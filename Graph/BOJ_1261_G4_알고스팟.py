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
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            if dist + board[nx][ny] < distance[nx][ny]:
                distance[nx][ny] = dist + board[nx][ny]
                heapq.heappush(que, (dist + board[nx][ny], nx, ny))
                

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(m)]
INF = 1e9
distance = [[INF]*(n) for _ in range(m)]

dijkstra(0, 0)
print(distance[m-1][n-1])
