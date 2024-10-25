import sys

P = int(sys.stdin.readline())

for _ in range(P):
    info = list(map(int, sys.stdin.readline().split()))
    idx, std = info[0], info[1:]
    count = 0
    for i in range(0,19):
        for j in range(i+1, 20):
            if std[i] > std[j]:
                std[i], std[j] = std[j], std[i]
                count += 1
    print(idx, count)