import sys

H, W = map(int ,sys.stdin.readline().split())
cloud = [list(sys.stdin.readline().strip()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if cloud[i][j] != 'c':
            continue
        
        temp_i = i
        temp_j = j
        cnt = 0
        temp = cloud[temp_i][temp_j]
        while temp != 'c' or temp_j <= W:
            if temp == 'c':
                cnt = 0
                cloud[temp_i][temp_j] = cnt
                if temp_j == W-1:
                    break
                temp_j += 1
                cnt += 1
                temp = cloud[temp_i][temp_j]
            else:
                cloud[temp_i][temp_j] = cnt
                if temp_j == W-1:
                    break
                temp_j += 1
                cnt += 1
                temp = cloud[temp_i][temp_j]

for cloud_row in cloud:
    for cloud_num in cloud_row:
        if cloud_num == '.':
            print(-1, end=' ')
        else:
            print(cloud_num, end=' ')
    print()