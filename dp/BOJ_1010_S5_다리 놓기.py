# 조합 : n! / (n-r)! * r!
import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    bridge = math.factorial(m) // (math.factorial(m-n)*math.factorial(n))
    print(bridge)