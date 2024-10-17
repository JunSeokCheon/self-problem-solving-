import sys

n, s = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
compare_length = 1e9
left, right = 0, 0
sum = 0

while True:  
    if sum >= s:
        compare_length = min(compare_length, right-left)
        sum -= num_list[left]
        left += 1
    elif right >= n:
        break
    else:
        sum += num_list[right]
        right += 1
        
if compare_length == 1e9:
    print(0)
else:
    print(compare_length)