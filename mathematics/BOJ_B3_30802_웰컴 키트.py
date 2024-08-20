import sys, math

N = int(sys.stdin.readline())
shirts = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())
t_num = 0

for shirt in shirts:
    t_num += (math.ceil(shirt/T))

print(t_num)
print(N//P, N%P)