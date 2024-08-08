import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

paper_num = int(sys.stdin.readline())
board = [[0 for _ in range(101)] for _ in range(101)]
result = 0
for _ in range(paper_num):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            board[i][j] = 1

for i in range(101):
    for j in range(101):
        if board[i][j] == 1:
            temp_value = 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if board[ni][nj] == 1:
                    temp_value += 1
            
            if temp_value == 3:
                result += 1
            elif temp_value == 2:
                result += 2
print(result)