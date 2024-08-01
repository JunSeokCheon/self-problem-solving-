# 실패
# import sys

# def coordinate_transformations(direct, coordinate, dist):
#     # 1: 북쪽, 2: 남쪽, 3: 서쪽, 4: 동쪽
#     if direct == 1:
#         coordinate.append([dist, height])
#     elif direct == 2:
#         coordinate.append([dist, 0])
#     elif direct == 3:
#         coordinate.append([0, height-dist])
#     elif direct == 4:
#         coordinate.append([width, height-dist])

# width, height = map(int, sys.stdin.readline().split())
# store_num = int(sys.stdin.readline())
# coordinate = []
# donggeun_coordinate = []
# for _ in range(store_num):
#     direct, dist = map(int, sys.stdin.readline().split())
#     coordinate_transformations(direct, coordinate, dist)
# donggeun_direct, donggeun_dist = map(int, sys.stdin.readline().split())
# coordinate_transformations(donggeun_direct, donggeun_coordinate, donggeun_dist)
# result = 0

# print(coordinate)
# print(donggeun_coordinate)

# for cord in coordinate:
#     if cord[0] == donggeun_coordinate[0][0] or cord[1] == donggeun_coordinate[0][1]:
#         correct = abs(cord[0]-donggeun_coordinate[0][0]) + abs(cord[1]-donggeun_coordinate[0][1])
#     elif cord[0] == 0:
#         correct = sum(cord) + sum(donggeun_coordinate[0])
#     elif cord[0] == width:
#         correct = (width - donggeun_coordinate[0][0]) + cord[1]
#     else:
#         opt1 = sum(cord) + sum(donggeun_coordinate[0])
#         opt2 = (width - donggeun_coordinate[0][0]) + (height - donggeun_coordinate[0][1]) + cord[0]
#         correct = min(opt1, opt2)
#     result += correct
# print(result)
    
import sys

def relative_distance(direction, dist):
    if direction == 1:
        return dist
    elif direction == 4:
        return width + dist
    elif direction == 2:
        return width + height + width - dist
    elif direction == 3:
        return width + height + width + height - dist

width, height = map(int, sys.stdin.readline().split())
store_num = int(sys.stdin.readline())
dist_list = []
result = 0

for _ in range(store_num+1):
    direction, dist = map(int, sys.stdin.readline().split())
    dist_list.append(relative_distance(direction, dist))

donggune = dist_list[-1]

for i in range(store_num):
    distance = abs(donggune-dist_list[i])
    total = 2*(width+height)
    result += min(distance, total - distance)
print(result)