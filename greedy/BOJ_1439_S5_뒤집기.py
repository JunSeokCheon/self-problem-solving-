import sys
from collections import defaultdict

s = sys.stdin.readline().strip()
mini_s_dic = defaultdict(int)
inflection_point = s[0]
mini_s_dic[inflection_point] += 1

if len(set(s)) == 1:
    print(0)
else:
    for mini_s in s:
        if mini_s != inflection_point:
            inflection_point = mini_s
            mini_s_dic[inflection_point] += 1
            
    print(min(mini_s_dic.values()))