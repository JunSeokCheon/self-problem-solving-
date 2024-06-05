# 해당 문제는 가장 작은 수 2개를 뽑아서 처리해주는 로직이 필요하다.
# 가장 작은 수를 찾는 알고리즘이 중요한데, sort를 사용할 시 시간복잡도는 nlogn으로 조건에 초과된다.
# 최소힙을 사용하여 항상 앞에 있는 수가 최소값을 보장해주는 성질을 이용해서 풀이한다.
# 핵심 : 최소힙
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