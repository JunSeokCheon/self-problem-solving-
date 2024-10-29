import sys

game_type = {'Y':1, 'F':2, 'O':3}
N, type = map(str, sys.stdin.readline().strip().split())
players = []
for _ in range(int(N)):
    player = sys.stdin.readline().strip()
    players.append(player)

pre_players = set(players)
print(len(pre_players)//game_type[type])