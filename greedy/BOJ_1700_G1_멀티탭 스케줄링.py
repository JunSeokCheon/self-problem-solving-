# 그냥 가장 많이 사용할 전기 용품을 뺀다면, 뒤에 많이 몰려있는 경우 반례가 생김.
# 남은 사용 중에 가장 늦게 사용되는 것을 뽑자

import sys

n, k = map(int, sys.stdin.readline().split())
k_list = list(map(int, sys.stdin.readline().split()))
contain = []
result = 0

for elect in range(k):
    if k_list[elect] in contain:
        continue

    if len(contain) < n:
        contain.append(k_list[elect])
        continue
    
    # 우선순위 리스트 선언
    prior = []
    # 다시 이용 여부 파악
    for c in contain:
        if c in k_list[elect:]:
            prior.append(k_list[elect:].index(c))
        else:
            prior.append(101)
    
    target = prior.index(max(prior))
    contain.remove(contain[target])
    contain.append(k_list[elect])
    result += 1

print(result)