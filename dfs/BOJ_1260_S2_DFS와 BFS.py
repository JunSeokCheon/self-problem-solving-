import sys
from collections import deque

def bfs(graph, visited, v):
    que = deque()
    que.append(v)
    visited[v] = 1
    print(v, end=' ')

    while que:
        x = que.popleft()

        for edge in sorted(graph[x]):
            if visited[edge] == 0:
                que.append(edge)
                visited[edge] = 1
                print(edge, end=' ')

def dfs(graph, visited, v):
    visited[v] = 1
    print(v, end=' ')

    for edge in sorted(graph[v]):
        if visited[edge] == 0:
            dfs(graph, visited, edge)


n, k, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(k):
    num1, num2 = map(int, sys.stdin.readline().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

dfs(graph, visited, v)
visited = [0] * (n+1)
print()
bfs(graph, visited, v)