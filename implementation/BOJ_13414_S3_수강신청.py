import sys
from collections import defaultdict

K, L = map(int, sys.stdin.readline().split())
waiting_dict = defaultdict(int)

for _ in range(L):
    std_num = sys.stdin.readline().strip()
    if std_num in waiting_dict:
        del waiting_dict[std_num]
        waiting_dict[std_num] = 1
    else:
        waiting_dict[std_num] = 1

for result in list(waiting_dict.keys())[:K]:
    print(result)