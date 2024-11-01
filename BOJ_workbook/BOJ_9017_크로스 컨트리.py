import sys
from collections import Counter, defaultdict

T = int(sys.stdin.readline())
for _ in range(T):
    score_dict = defaultdict(list)
    result = []
    sum_score = 1e9
    N = int(sys.stdin.readline())
    team_list = list(map(int, sys.stdin.readline().split()))
    exclude_team = []
    
    for key, value in Counter(team_list).items():
        if value != 6:
            exclude_team.append(key)
    
    team_list = [i for i in team_list if i not in exclude_team]

    for idx, team in enumerate(team_list):
        score_dict[team].append(idx+1)
    
    for key, values in score_dict.items():
        if sum_score >= sum(values[:4]):
            sum_score = sum(values[:4])
    
    for key, values in score_dict.items():
        if sum(values[:4]) == sum_score:
            result.append([key, values[4]])
    
    result = sorted(result, key = lambda x: x[1])
    print(result[0][0])