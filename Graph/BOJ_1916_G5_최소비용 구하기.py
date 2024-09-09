import sys, heapq

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    
    while que:
        dist, now_node = heapq.heappop(que)
        
        if distance[now_node] < dist:
            continue
        
        for i in graph[now_node]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(que, (dist + i[1], i[0]))

INF = 1e9
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))
    
start, end = map(int, sys.stdin.readline().split())    

dijkstra(start)
print(distance[end])