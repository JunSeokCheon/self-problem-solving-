import sys
from itertools import permutations

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

for i in range(n-1, 0,-1):
    if n_list[i-1] > n_list[i]:
        for j in range(n-1, 0, -1):
            if n_list[i-1] > n_list[j]:
                n_list[i-1], n_list[j] = n_list[j], n_list[i-1]
                n_list = n_list[:i] + sorted(n_list[i:], reverse=True)
                print(*n_list)
                exit(0)
print(-1)