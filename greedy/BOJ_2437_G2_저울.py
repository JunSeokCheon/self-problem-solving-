# 실패 - 11%
# import sys

# n = int(sys.stdin.readline())
# n_list = list(map(int, sys.stdin.readline().split()))
# init_range = [0, 0]

# n_list.sort()

# for num in n_list:
#     compare_range = [init_range[0]+num, init_range[1]+num]
#     if compare_range[0] <= init_range[1] + 1:
#         init_range[1] += num
#     else:
#         print(init_range[1]+1)
#         break

# 예제
# 5
# 1 1 1 1 1 -> 6

# 10
# 1 2 4 8 16 32 64 128 256 512 1024 -> 2048

# 1
# 2 -> 1
import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
init_range = [0, 0]
flag = True
result = 0

n_list.sort()

for num in n_list:
    compare_range = [init_range[0]+num, init_range[1]+num]
    if compare_range[0] <= init_range[1] + 1:
        init_range[1] += num
        result = init_range[1] + 1
    else:
        result = init_range[1] + 1
        flag = False
        break

print(result)