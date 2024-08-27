import sys

N = int(sys.stdin.readline())
provinces = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())
provinces.sort()
start = 0
end = provinces[-1]

while start <= end:
    mid = (start+end)//2
    total = 0
    
    for province in provinces:
        if province > mid:
            total += mid
        else:
            total += province
            
    if total > budget:
        end = mid - 1
    else:
        start = mid + 1

print(end)