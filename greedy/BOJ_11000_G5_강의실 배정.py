import sys
import heapq

N = int(sys.stdin.readline().strip())
n_list = []

for _ in range(N):
    s, t = map(int, sys.stdin.readline().split())
    n_list.append([s, t])

n_list = sorted(n_list, key = lambda x : x[0])
heap = [n_list[0][1]]

for i in range(1, N):
    if heap[0] <= n_list[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, n_list[i][1])

print(len(heap))