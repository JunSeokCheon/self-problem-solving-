import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
jewel = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]
result = 0

jewel.sort()
bags.sort()

heap = []
for bag in bags:
    while jewel and jewel[0][0] <= bag:
        heapq.heappush(heap, -jewel[0][1])
        heapq.heappop(jewel)
    if heap:
        result -= heapq.heappop(heap)

print(result)