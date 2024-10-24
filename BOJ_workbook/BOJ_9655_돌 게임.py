# N = 1, 선공 승
# N = 2, 후공 승
# N = 3, 선공 승
# N = 4, 후공 승
# N = 5, 선공 승
# N이 홀수면 선공 승, 짝수면 후공 승

import sys

n = int(sys.stdin.readline())
print('SK' if n%2 != 0 else 'CY')