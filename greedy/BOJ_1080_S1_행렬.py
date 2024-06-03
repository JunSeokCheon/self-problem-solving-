import sys

n, m  = map(int, sys.stdin.readline().split())
n_list = []
m_list = []
result = 0

for _ in range(n):
    n_list.append(list(map(int,sys.stdin.readline().strip())))

for _ in range(n):
    m_list.append(list(map(int,sys.stdin.readline().strip())))

if n_list == m_list:
    print(0)
    exit(0)
else:
    for i in range(n-2):
        for j in range(m-2):
            if n_list[i][j] != m_list[i][j]:
                result += 1
                for k in range(i, i+3):
                    for v in range(j, j+3):
                        n_list[k][v] = 1- n_list[k][v]
    
    if n_list == m_list:
        print(result)
        exit(0)
    else:
        print(-1)
        exit(0)