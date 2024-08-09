import sys

P = int(sys.stdin.readline())
for _ in range(P):
    child = list(map(int, sys.stdin.readline().split()))
    walk_count = 0
    
    for i in range(1, 20):
        for j in range(i+1, 21):
            if child[i] > child[j]:
                child[i], child[j] = child[i], child[j]
                walk_count += 1
    print(child[0], walk_count)