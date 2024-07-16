import sys

def check(num):
    for i in range(n-num+1):
        for j in range(m-num+1):
            if rect[i][j] == rect[i][j+num-1] == rect[i+num-1][j] == rect[i+num-1][j+num-1]:
                return True
    return False


n, m = map(int, sys.stdin.readline().split())
rect = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

size = min(n,m)

for i in range(size, 0, -1):
    if check(i):
        print(i**2)
        break