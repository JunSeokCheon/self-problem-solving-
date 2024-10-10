# 시간초과
# import sys

# h, w, n, m = map(int, sys.stdin.readline().split())
# board = [[0]*w for _ in range(h)]
# result = 0

# for i in range(0, h, n+1):
#     for j in range(0, w, m+1):
#         board[i][j] = 1

# for mini_result in board:
#     result += sum(mini_result)

# print(result)

# 규칙성을 발견하자
# 5칸 - 간격 1 -> 3명 -> 5/1+1 -> 2.5
# 5칸 - 간격 2 -> 2명 -> 5/2+1 -> 1.66
# 5칸 - 간격 3 -> 2명 -> 5/3+1 -> 1.33
# 5칸 - 간격 4 -> 1명 -> 5/4+1 -> 1
import sys, math

h, w, n, m = map(int, sys.stdin.readline().split())

h = math.ceil(h/(n+1))
w = math.ceil(w/(m+1))
print(h*w)