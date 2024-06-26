# 에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.

# 이 알고리즘은 다음과 같다.

# 2부터 N까지 모든 정수를 적는다.
# 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
# P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
# N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.
# 7 3 -> 6
# 15 12 -> 7
# 10 7 -> 9

import sys

n, k = map(int, sys.stdin.readline().split())
n_list = [num for num in range(2, n+1)]
remove_count = 0
result = 0

try:
    while n_list:
        min_num = min(n_list)
        for num in n_list:
            if num%min_num == 0:
                n_list.remove(num)
                remove_count += 1
                if remove_count == k:
                    result = num
                    raise NotImplementedError
except:
    print(result)