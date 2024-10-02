import sys, heapq

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    
    while que:
        dist, node = heapq.heappop(que)
        
        if dist > distance[node]:
            continue
        
        for node_info in maps[node]:
            if dist + node_info[1] < distance[node_info[0]]:
                distance[node_info[0]] = dist + node_info[1]
                heapq.heappush(que, (dist + node_info[1], node_info[0]))

INF = 1e9
n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
maps = [[]*(n+1) for _ in range(n+1)]
result = 0

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    maps[a].append((b,l))
    maps[b].append((a,l))

for area in range(1, n+1):
    distance = [INF] * (n+1)
    dijkstra(area)
    
    temp = 0
    for idx, dist in enumerate(distance):
        if dist <= m:
            temp += items[idx-1]
    
    result = max(temp, result)

print(result)