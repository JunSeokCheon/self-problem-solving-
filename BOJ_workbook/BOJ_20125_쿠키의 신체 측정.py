import sys

N = int(sys.stdin.readline())
cookie = [list(sys.stdin.readline().strip()) for _ in range(N)]
head_x, head_y = 0, 0
flag = 0
for i in range(N):
    for j in range(N):
        if cookie[i][j] == '*':
            head_x, head_y = i, j
            flag = 1
            break
    if flag:
        break

heart_x, heart_y = head_x+1, head_y
left_arm = 0
right_arm = 0
back = 0
left_leg = 0
right_leg = 0

# 왼쪽 팔
for i in range(heart_y-1, -1, -1):
    if cookie[heart_x][i] == '*':
        left_arm += 1
    else:
        break

# 오른쪽 팔
for i in range(heart_y+1, N, 1):
    if cookie[heart_x][i] == '*':
        right_arm += 1
    else:
        break

# 허리
for i in range(heart_x+1, N, 1):
    if cookie[i][heart_y] == '*':
        back += 1
    else:
        break

leg_standard = i
# 왼쪽 다리
for i in range(leg_standard, N, 1):
    if cookie[i][heart_y-1] == '*':
        left_leg += 1
    else:
        break
 
# 오른쪽 다리
for i in range(leg_standard, N, 1):
    if cookie[i][heart_y+1] == '*':
        right_leg += 1
    else:
        break

print(heart_x+1, heart_y+1)
print(left_arm, right_arm, back, left_leg, right_leg)