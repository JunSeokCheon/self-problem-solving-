# 투 포인터(Two Pointers)

- 투 포인터 알고리즘은 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘이다.
- 시작점과 끝점 2개의 점으로 접근할 데이터의 범위를 표현한다.
- 부분합 예시를 보면서 이해하는 것이 좋다.

---
## 예시 : 부분합

- 부분합 문제 : N칸의 1차원 배열이 있을 때, 부분 배열 중 그 원소의 합이 M이 되는 경우의 수를 구하는 것
- 모든 경우의 수를 구하면 O(N^2)가 되기 때문에, 시간복잡도가 크다.

### 투 포인터 사용

- 포인터 2개를 준비한다. (start, end)
- 맨 처음은 start = end = 0이며, 항상 start <= end를 만족해야 한다.
- 2개의 포인터의 역할은 현재 부분 배열의 시작과 끝을 가르킨다.

* s = e의 경우는 크기가 0, 아무것도 포함하지 않는 부분 배열을 뜻한다.

아래의 과정을 s < N인 동안 반복한다.
1. 만약 현재 부분합이 M 이상이거나, 이미 e = N이면 start++
2. 그렇지 않다면 end++
3. 현재 부분합이 M과 같다면 최종 결과++

* 정리하자면, start와 end를 무조건 증가시키는 방향으로만 변화시켜 도중에 부분 배열의 합이 정확히 M이 되는 경우를 세는 것이다.

### 파이썬 코드

1. 부분합이 5인 경우의 수 구하기
```python
n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
```


2. 백준 - 과일 탕후루 문제(https://www.acmicpc.net/problem/30804)
```python
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
```
