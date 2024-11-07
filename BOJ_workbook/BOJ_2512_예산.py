# 반례
# 5
# 100 100 100 100 100
# 10
# 2
import sys

N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
total = int(sys.stdin.readline())

if sum(budgets) <= total:
    print(max(budgets))
else:
    start = 1
    end = max(budgets)
    
    while start <= end:
        middle = (start + end) // 2
        temp_sum = 0
        
        for budget in budgets:
            if budget >= middle:
                temp_sum += middle
            else:
                temp_sum += budget
        
        if temp_sum > total:
            end = middle -1
        else:
            start = middle + 1
    print(end)