import sys

nums =sys.stdin.readline().strip()
result = 0
idx = 0
while True:
    result += 1
    for mini_result in str(result):
        if nums[idx] == mini_result:
            idx += 1
            if len(nums) <= idx:
                print(result)
                exit(0)