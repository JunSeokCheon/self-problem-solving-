import sys

n, k = map(int, sys.stdin.readline().split())
olympics = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

olympics.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

goal_idx = [olympics[i][0] for i in range(n)].index(k)

for i in range(n):
    if olympics[goal_idx][1:] == olympics[i][1:]:
        print(i+1)
        break