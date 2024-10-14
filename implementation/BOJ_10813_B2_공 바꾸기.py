import sys

n, m = map(int, sys.stdin.readline().split())
balls = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    temp = 0
    temp = balls[i]
    balls[i] = balls[j]
    balls[j] = temp

print(*balls[1:])