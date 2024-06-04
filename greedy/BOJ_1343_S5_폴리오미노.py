import sys

board = sys.stdin.readline()
poly_list = ['AAAA', 'BB']

if len(board) < 2:
    print(-1)
    exit(0)

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if "X" in board:
    print(-1)
else:
    print(board)