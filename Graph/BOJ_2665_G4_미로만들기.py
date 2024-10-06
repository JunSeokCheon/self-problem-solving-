import sys, heapq

def dijkstra(x, y):
    que = []
    heapq.heappush(que, (0, x, y))
    distance[x][y] = 1
    
    while que:
        dist, a, b = heapq.heappop(que)
        
        if a == n-1 and b == n-1:
            return dist
        
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if distance[nx][ny] == 0:
                distance[nx][ny] = 1
                if board[nx][ny] == 0:
                    heapq.heappush(que, (dist+1, nx, ny))
                else:
                    heapq.heappush(que, (dist, nx, ny))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
distance = [[0]*(n) for _ in range(n)]

print(dijkstra(0,0))

# import sys, heapq

# def dijkstra(x,y):
#     que = []
#     heapq.heappush(que, (0, x, y))
#     visited[x][y] = 1
    
#     while que:
#         dist, a, b = heapq.heappop(que)
        
#         if a == n-1 and b == n-1:
#             return dist
        
#         for k in range(4):
#             nx = a + dx[k]
#             ny = b + dy[k]
            
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
            
#             if visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 if board[ny][ny] == 0:
#                     heapq.heappush(que, (dist+1, nx, ny))
#                 else:
#                     heapq.heappush(que, (dist, nx, ny))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# n = int(sys.stdin.readline())
# board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
# visited = [[0]*n for _ in range(n)]

# print(dijkstra(0,0))
