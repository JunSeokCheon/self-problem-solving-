import sys

n, l = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
result = 1
n_list.sort()

standard_start = n_list[0] - 0.5
standard_end = n_list[0] - 0.5 + l

for n_num in n_list:
    if standard_start <= n_num <= standard_end:
        pass
    else:
        result += 1
        standard_start = n_num - 0.5
        standard_end = n_num - 0.5 + l

print(result)




