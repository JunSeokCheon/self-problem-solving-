import sys

n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for _ in range(n)]
result = 0
standard_num = n_list[n-1]
for idx in range(len(n_list)-2, -1, -1):
    while standard_num <= n_list[idx]:
        result += 1
        n_list[idx] -= 1
    standard_num = n_list[idx]
print(result)