import sys, heapq

def dijkstra(n):
    distance[n] = 0
    que = []
    heapq.heappush(que, (0, n))
    
    while que:
        dist, node = heapq.heappop(que)
        
        if distance[node] < dist:
            continue
        
        for move_node in (node-1, node+1, node*2):
            if move_node < 0 or move_node > 100000:
                continue
        
            cost = dist
            if move_node != node*2:
                cost = dist + 1
                
            if cost < distance[move_node]:
                distance[move_node] = cost
                heapq.heappush(que, (cost, move_node))
            
n, k = map(int, sys.stdin.readline().split())
INF = 1e9
distance = [INF] * (100001)

dijkstra(n)
print(distance[k])