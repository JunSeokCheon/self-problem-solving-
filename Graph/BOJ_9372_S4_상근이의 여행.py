import sys

def dfs(node, result):
    visited[node] = 1
    
    for node_coord in graph[node]:
        if visited[node_coord] == 0:
            result = dfs(node_coord, result+1)
    return result

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print(dfs(1, 0))