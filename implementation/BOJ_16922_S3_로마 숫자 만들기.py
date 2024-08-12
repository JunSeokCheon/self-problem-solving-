import sys
from itertools import combinations_with_replacement

ROMA = [1, 5, 10, 50]

N = int(sys.stdin.readline())
result = []
for num_tuple in list(combinations_with_replacement(ROMA, N)):
    result.append(sum(num_tuple))
print(len(set(result)))