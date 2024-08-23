# 핵심 반례
# 6 5
# 1 6
# 2 4 5
# 2 1 2
# 2 2 3
# 2 3 4
# 2 5 6

# -> 0
import sys

N, M = map(int, sys.stdin.readline().split())
truth = list(map(int, sys.stdin.readline().split()))
parties = []
result = 0

for _ in range(M):
    party = list(map(int, sys.stdin.readline().split()))
    parties.append(party[1:])
    
if truth == 0:
    print(M)
    exit(0)

truth = set(truth[1:])
for _ in range(M):
    for party in parties:
        if len(set(party)&truth) > 0:
            truth = truth | set(party)

for party in parties:
    if len(truth & set(party))==0:
        result += 1

print(result)