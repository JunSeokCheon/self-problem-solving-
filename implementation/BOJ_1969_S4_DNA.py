import sys

N, M = map(int, sys.stdin.readline().split())
DNA_list = [sys.stdin.readline().strip() for _ in range(N)]
result = ''
cnt = 0

for i in range(M):
    # A, C, G, T
    count = [0, 0, 0, 0]
    for j in range(N):
        if DNA_list[j][i] == 'A':
            count[0] += 1
        elif DNA_list[j][i] == 'C':
            count[1] += 1
        elif DNA_list[j][i] == 'G':
            count[2] += 1
        else:
            count[3] += 1
    max_idx = count.index(max(count))

    if max_idx == 0:
        result += 'A'
    elif max_idx == 1:
        result += 'C'
    elif max_idx == 2:
        result += 'G'
    elif max_idx == 3:
        result += 'T'
    cnt += N - max(count)

print(result)
print(cnt)