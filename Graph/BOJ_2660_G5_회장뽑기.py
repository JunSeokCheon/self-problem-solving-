import sys

INF = 1e9
n = int(sys.stdin.readline())
graph = [[INF]*(n+1) for _ in range(n+1)]

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1
    
for i in range(1, n+1):
    graph[i][i] = 0
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
result = [INF] * (n+1)
for idx, div_graph in enumerate(graph):
    result[idx] = max(div_graph[1:])

min_num = min(result)
print(min_num, result.count(min_num))

for idx, num in enumerate(result):
    if num == min_num:
        print(idx, end=' ')