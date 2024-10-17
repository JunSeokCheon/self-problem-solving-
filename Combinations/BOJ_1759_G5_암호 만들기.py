from itertools import combinations, permutations
import sys

l, c = map(int, sys.stdin.readline().split())
char_list = list(map(str, sys.stdin.readline().split()))
result = []

for num in combinations(sorted(char_list), l):
    opt1 = 0
    opt2 = 0
    
    for mini_num in num:
        if mini_num in ['a', 'e', 'i', 'o', 'u']:
            opt1 += 1
        else:
            opt2 += 1
    
    if opt1 >= 1 and opt2 >= 2:
        print(''.join(num))
