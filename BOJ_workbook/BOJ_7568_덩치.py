import sys

n = int(sys.stdin.readline())
info = []
for idx in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    info.append([weight, height])
    
for i in range(len(info)):
    rank = 1
    for j in range(len(info)):
        if (info[i][0] < info[j][0]) and (info[i][1] < info[j][1]):
            rank += 1
    print(rank, end=' ')
