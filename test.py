import sys

n, k = map(int, sys.stdin.readline().split())
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

n_list.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

goal_index = [n_list[i][0] for i in range(n)].index(k)

for i in range(n):
    if n_list[goal_index][1:] == n_list[i][1:]:
        print(i+1)
        break
