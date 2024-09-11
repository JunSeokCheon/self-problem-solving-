# * 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.*
import sys

INF = 1e9
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a][b] > c:
        graph[a][b] = c

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for result in graph[1:]:
    print(*result[1:])