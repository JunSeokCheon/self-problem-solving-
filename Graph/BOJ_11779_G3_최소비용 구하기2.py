import sys, heapq

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    
    while que:
        dist, node = heapq.heappop(que)
        
        if dist > distance[node]:
            continue

        for node_info in graph[node]:
            if dist + node_info[1] < distance[node_info[0]]:
                distance[node_info[0]] = dist + node_info[1]
                heapq.heappush(que, (dist + node_info[1], node_info[0]))
                parents[node_info[0]] = node
                
INF = 1e9
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[]*(n+1) for _ in range(n+1)]
distance = [INF] * (n+1)
parents = [0] * (n+1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

start, end = map(int, sys.stdin.readline().split())

dijkstra(start)
print(distance[end])

path = []
cur = end
while cur:
    path.append(cur)
    cur = parents[cur]
print(len(path))
print(*reversed(path))