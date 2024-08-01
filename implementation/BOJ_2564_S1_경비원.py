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

#북쪽 왼쪽 모서리를 0으로 잡고 펼쳤을 때 0으로부터 얼마나 떨어졌는 지 위치를 계산해주는 함수
def cal_dist(loc, distance) :
    if loc==1 : #북쪽
        return distance
    elif loc==4 : #동쪽
        return w+distance
    elif loc==2 : #남쪽
        return w+h+w-distance
    elif loc==3 : #서쪽
        return w+h+w+h-distance

#블록의 가로길이 세로길이 입력받기
w, h = map(int,input().split())

#상점의 개수 입력받기
num=int(sys.stdin.readline())

dist=[]
#각 상점의 위치와 동근이의 위치 입력받기
for _ in range(num+1) :
    loc, distance=map(int, sys.stdin.readline().split())
    dist.append(cal_dist(loc, distance))

#동근이 거리
dong_dist=dist[-1]

answer=0
for i in range(num):
    #0에서 떨어진 각 가게의 거리와, 0에서 떨어진 동근의 위치 차이의 절댓값을 구해준다.
    cal_distance=abs(dist[i]-dong_dist)

    #전체 길이를 구해준다.
    total=2*(w+h)

    #더 작은 값을 answer에 누적시킨다.
    answer+=min(cal_distance,total-cal_distance)

print(answer)