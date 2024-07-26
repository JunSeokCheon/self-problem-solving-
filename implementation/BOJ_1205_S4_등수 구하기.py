import sys

n, new, p = map(int, sys.stdin.readline().split())
if n == 0:
    print(1)
else:
    rank = list(map(int, sys.stdin.readline().split()))
    if n == p and rank[-1] >= new:
        print(-1)
    else:
        result = n + 1
        for i in range(n):
            if rank[i] <= new:
                result = i + 1
                break
        print(result)