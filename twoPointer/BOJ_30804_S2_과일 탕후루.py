# 투포인터 - 현재 꽂혀있는 과일들의 종류 세기
import sys

N = int(sys.stdin.readline())
fruits = list(map(int, sys.stdin.readline().split()))

left = 0
result = 0
fruits_count = {}
distinct_fruit = 0

for right in range(N):
    if fruits[right] in fruits_count:
        fruits_count[fruits[right]] += 1
    else:
        fruits_count[fruits[right]] = 1
        distinct_fruit += 1

    while distinct_fruit > 2:
        fruits_count[fruits[left]] -= 1
        if fruits_count[fruits[left]] == 0:
            del fruits_count[fruits[left]]
            distinct_fruit -= 1
        left += 1
    
    result = max(result, right-left+1)
        
print(result)