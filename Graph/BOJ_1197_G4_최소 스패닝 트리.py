# 최소 스패닝 트리 - 크루스칼(union-find) 알고리즘, 프림 알고리즘
import sys
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, sys.stdin.readline().split())
graph = []
result = 0 
parent = [i for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append([c, a, b])

graph.sort()

for i in graph:
    cost, node1, node2 = i
    if find(node1) != find(node2):
        union(node1, node2)
        result += cost

print(result)