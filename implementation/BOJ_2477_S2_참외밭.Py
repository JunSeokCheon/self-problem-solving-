# 전체 사각형 - 작은 사각형 -> 참외밭
# 가장 긴 가로와 세로의 양 꼭지점과 접한 선분을 빼면 작은 삼각형의 넓이를 구할 수 있다.
import sys

k = int(sys.stdin.readline())
melon = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]

long_width = 0
long_width_idx = 0
long_height = 0
long_height_idx = 0

for i in range(len(melon)):
    if melon[i][0] == 1 or melon[i][0] == 2:
        if long_width < melon[i][1]:
            long_width = melon[i][1]
            long_width_idx = i
    elif melon[i][0] == 3 or melon[i][0] == 4:
        if long_height < melon[i][1]:
            long_height = melon[i][1]
            long_height_idx = i


short_width = abs(melon[(long_height_idx-1)%6][1] - melon[(long_height_idx+1)%6][1])
short_height = abs(melon[(long_width_idx-1)%6][1] - melon[(long_width_idx+1)%6][1])

result = (long_width*long_height) - (short_width*short_height)

print(result*k)