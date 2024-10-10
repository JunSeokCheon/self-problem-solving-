# 1(1), 2/3/4/5/6/7(2) -> 8-19(3) -> 20-37(4) -> 38-61(5)
# 1(1), 6(2) -> 12(3) -> 18(4) -> 24(6)

import sys

N = int(sys.stdin.readline())
result = 1
standard_num = 1
multi_idx = 1

while True:
    if N > standard_num:
        standard_num += 6*multi_idx
        multi_idx += 1
        result += 1
    else:
        break
print(result)