import sys
from collections import deque

def bfs():
    while que:
        x = que.popleft()
        for nodes in graph[x]:
            if parent_nodes[nodes] == 0:
                que.append(nodes)
                parent_nodes[nodes] = x

N = int(sys.stdin.readline())
graph = [[]*(N+1) for _ in range(N+1)]
parent_nodes = [0] * (N+1)

for _ in range(N-1):
    first_edge, second_edge = map(int, sys.stdin.readline().split())
    graph[first_edge].append(second_edge)
    graph[second_edge].append(first_edge)

que = deque()
que.append(1)
bfs()

for result in parent_nodes[2:]:
    print(result)