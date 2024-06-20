import sys

def dfs(x,y):
    global answer

    board[x][y] = 'start'

    if y == c-1:
        answer += 1
        return True

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if board[nx][ny] == '.':
            if dfs(nx,ny):
                return True
    
    return False

r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]
answer = 0

dx = [-1, 0, 1]
dy = [1, 1, 1]

for i in range(r):
    dfs(i, 0)

print(answer)