from collections import deque
import sys

N = int(sys.stdin.readline())
num_list = deque([num for num in range(1, N+1)])

while len(num_list) != 1:
    pop_num_first = num_list.popleft()
    pop_num_second = num_list.popleft()
    num_list.append(pop_num_second)

print(num_list[0])
