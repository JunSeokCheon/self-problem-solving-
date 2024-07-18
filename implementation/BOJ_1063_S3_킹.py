import sys

move_dic = {
    'R':(1,0),
    'L':(-1,0),
    'B':(0,-1),
    'T':(0,1),
    'RT':(1,1),
    'LT':(-1,1),
    'RB':(1,-1),
    'LB':(-1,-1),
}

alpha_dic = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}
reverse_alpha_dic = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H"}

king, stone, n = map(str, sys.stdin.readline().split())
move_list = [sys.stdin.readline().strip() for _ in range(int(n))]
trans_king = (alpha_dic[king[0]], int(king[1]))
trans_stone = (alpha_dic[stone[0]], int(stone[1]))

for move in move_list:
    move_x, move_y = move_dic[move]
    move_king = (trans_king[0]+move_x, trans_king[1]+move_y)
    move_stone = (trans_stone[0]+move_x, trans_stone[1]+move_y)

    if move_king[0] < 1 or move_king[0] > 8 or move_king[1] < 1 or move_king[1] > 8:
        pass
    else:
        if (move_king == trans_stone) and (move_stone[0] < 1 or move_stone[0] > 8 or move_stone[1] < 1 or move_stone[1] > 8):
            # print(trans_king, trans_stone)  
            pass
        else:
            if move_king == trans_stone:
                trans_king = move_king
                trans_stone = move_stone
            else:
                trans_king = move_king
print(reverse_alpha_dic[trans_king[0]] + str(trans_king[1]))
print(reverse_alpha_dic[trans_stone[0]] + str(trans_stone[1]))