import sys

a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))[::-1]
cal = 0
result = []

for i in range(m):
    cal += m_list[i]*(a**i)

while cal != 0:
    result.append(cal%b)
    cal //= b

print(' '.join(map(str, result[::-1])))