import sys
from itertools import permutations

n = int(sys.stdin.readline())
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = []

for idx, number in enumerate(n_list):
    temp_max = 0
    for set_number in set(list(permutations(number, 3))):
        unit_digit = int(str(sum(set_number))[-1])
        temp_max = max(temp_max, unit_digit)
    result.append((idx+1, temp_max))

final_result = sorted(result, key=lambda x : (-x[1], -x[0]))
print(final_result[0][0])