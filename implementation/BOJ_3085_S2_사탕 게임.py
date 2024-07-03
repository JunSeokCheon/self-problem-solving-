# 인접한 칸 -> 우측, 우측아래 확인((0,0)부터 탐색하면 좌측, 좌측위는 고려할 필요 없음)
import sys

# 같은 색 사탕 모두 먹는 로직(열, 행)
def check(board):
    max_cnt = 1
    for i in range(N):
        temp_cnt = 1
        # 열 확인
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                temp_cnt += 1
            else:
                temp_cnt = 1

            max_cnt = max(max_cnt, temp_cnt)
        
        # 행 확인
        temp_cnt = 1
        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                temp_cnt += 1
            else:
                temp_cnt = 1

            max_cnt = max(max_cnt, temp_cnt)
    
    return max_cnt

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]
result = 1

for i in range(N):
    for j in range(N):
        # 인접 열 확인 및 최대 범위 확인
        if j + 1 < N:
            # 인접 열 교환
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            # 같은 사탕 개수 확인
            cnt = check(board)
            # 최대 개수 갱신
            result = max(result, cnt)
            # 교환 원위치
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        
        # 인접 행 확인 및 최대 범위 확인
        if i + 1 < N:
            # 인접 열 교환
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            # 같은 사탕 개수 확인
            cnt = check(board)
            # 최대 개수 갱신
            result = max(result, cnt)
            # 교환 원위치
            board[i+1][j], board[i][j] = board[i][j], board[i+1][j]

print(result)