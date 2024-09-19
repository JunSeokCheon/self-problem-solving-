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
                heapq.heappush(que, (cost+node_info[1], node_info[0]))

n, m, x = map(int, sys.stdin.readline().split())
INF = 1e9
graph = [[]*(n+1) for _ in range(n+1)]
go_goal = [INF] * (n+1)
return_goal = [INF] * (n+1)
result = []
max_time = 0

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))

for start in range(1, n+1):
    distance = [INF] * (n+1)
    dijkstra(start)
    if start == x:
        return_goal = distance
    else:
        go_goal[start] = distance[x]

for go, turn in zip(go_goal, return_goal):
    result.append(go+turn)

for max_result in result[1:]:
    if max_result == INF:
        continue
    
    if max_time < max_result:
        max_time = max_result

print(max_time)