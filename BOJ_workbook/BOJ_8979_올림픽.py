import sys

n, k = map(int, sys.stdin.readline().split())
info = []
for _ in range(n):
    country, gold, sliver, bronze = map(int, sys.stdin.readline().split())
    info.append([country, gold, sliver, bronze])
    if country == k:
        target_medal = [gold, sliver, bronze]

sorted_info = sorted(info, key = lambda x: (x[1], x[2], x[3]), reverse=True)
# print(sorted_info)
flag = 1
result = 0
for i in range(n):
    if sorted_info[i][0] != k:
        if sorted_info[i][1:] == target_medal and flag:
            flag = 0
        elif sorted_info[i][1:] != target_medal:
            result += 1
    else:
        result += 1
        break
    
print(result)