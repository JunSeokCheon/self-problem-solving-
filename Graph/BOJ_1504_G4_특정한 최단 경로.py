import sys, heapq

def dijkstra(start, end):
    distance = [INF] * (n+1)
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
    
    return distance[end]

INF = 1e9
n, e = map(int, sys.stdin.readline().split())
graph = [[]*(n+1) for _ in range(n+1)]


for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())

# 1 -> v1 -> v2 -> n
path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)

# 1 -> v2 -> v1 -> n
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))