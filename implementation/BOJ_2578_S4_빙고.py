# 빙고 외치기(3개 이상) -> 가로/세로/대각선(2종류) 확인

# 반례 Example
# 1. 일반적인 반례
# Question
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
# 6 7 8 9 10
# 3 13 18 23 5
# 17 21 1 2 4
# 11 12 14 15 16
# 19 20 22 24 25 
# Answer
# 12

# 2. 빙고 개수가 1 -> 2 -> 4개가 될 때 (빙고 체크 조건문 확인)
# Question
# 9 10 1 11 12
# 13 14 2 15 16
# 3 4 17 5 6
# 18 19 7 20 21
# 22 23 8 24 25
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
# Answer
# 17

import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
check = [[0]*5 for _ in range(5)]
moderator = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
result = 0

def check_num(num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                check[i][j] = 1
                break

def check_bingo():
    count = 0

    # 가로
    for i in range(5):
        if sum(check[i]) == 5:
            count += 1

    # 세로
    for j in range(5):
        res = 0
        for i in range(5):
            if check[i][j] == 1:
                res += 1
        if res == 5:
            count += 1

    # 대각선(좌측상단 -> 우측하단)
    res = 0
    for i in range(5):
        if check[i][i] == 1:
            res += 1
    if res == 5:
        count += 1

    # 대각선(우측상단 -> 좌측하단)
    res = 0
    for i in range(5):
        if check[i][4-i] == 1:
            res += 1
    if res == 5:
        count += 1
    
    return count

for i in range(5):
    for j in range(5):
        check_num(moderator[i][j])
        result += 1
        if check_bingo() >= 3:
            print(result)
            exit(0)