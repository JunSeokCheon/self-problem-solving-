import sys, math

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
site = list(map(int, sys.stdin.readline().split()))
len_list = []

start = site[0] - 0
end = n - site[-1]
len_list.append(start)
len_list.append(end)

for i in range(1, len(site)):
    len_list.append(math.ceil((site[i]-site[i-1])/2))

print(max(len_list))