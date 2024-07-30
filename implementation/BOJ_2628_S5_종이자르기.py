import sys

width, height = map(int, sys.stdin.readline().split())
cnt = int(sys.stdin.readline())
width_list = [0, width]
height_list = [0, height]
result = 0

for _ in range(cnt):
    direct, num = map(int, sys.stdin.readline().split())
    if direct == 0:
        height_list.append(num)
    elif direct == 1:
        width_list.append(num)
        
width_list.sort()
height_list.sort()

for i in range(len(width_list)-1):
    for j in range(len(height_list)-1):
        cal_width = width_list[i+1] - width_list[i]
        cal_height = height_list[j+1] - height_list[j]
        result = max(result, cal_width*cal_height)
print(result)