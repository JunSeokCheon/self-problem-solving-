import sys, heapq

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    
    while que:
        cost, node = heapq.heappop(que)
        
        if cost > distance[node]:
            continue
        
        for node_info in graph[node]:
            if cost + node_info[1] < distance[node_info[0]]:
                distance[node_info[0]] = cost + node_info[1]
                heapq.heappush(que, (cost + node_info[1], node_info[0]))

INF = 1e9
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
distance = [1e9] * (V+1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dijkstra(K)
for dist in distance[1:]:
    if dist == INF:
        print("INF")
    else:
        print(dist)