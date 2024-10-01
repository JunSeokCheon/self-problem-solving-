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
            
            if dist + cave[nx][ny] < distance[nx][ny]:
                distance[nx][ny] = dist + cave[nx][ny]
                heapq.heappush(que, (dist + cave[nx][ny], nx, ny)) 


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

INF = 1e9
count = 0

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    count += 1
    cave = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    distance = [[INF]*(n) for _ in range(n)]
    
    dijkstra(0,0)
    print(f'Problem {count}: {distance[n-1][n-1] + cave[0][0]}')