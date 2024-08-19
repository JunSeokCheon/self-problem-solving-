import sys

N = int(sys.stdin.readline())
std_num = [sys.stdin.readline().strip() for _ in range(N)]
result = 1

for i in range(len(std_num[0])-1, -1, -1):
    temp_value_list = []
    for j in range(N):
        temp_value_list.append(std_num[j][i:])
    if len(set(temp_value_list)) == N:
        break
    result += 1
print(result)