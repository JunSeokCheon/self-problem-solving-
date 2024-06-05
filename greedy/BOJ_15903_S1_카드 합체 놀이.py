import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))

heapq.heapify(n_list)

for _ in range(m):
    first_num = heapq.heappop(n_list)
    second_num = heapq.heappop(n_list)
    sum_num = first_num + second_num
    heapq.heappush(n_list, sum_num)
    heapq.heappush(n_list, sum_num)
    
print(sum(n_list))