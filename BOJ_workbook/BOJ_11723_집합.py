import sys

M = int(sys.stdin.readline())
S = []
for _ in range(M):
    operations = list(map(str, sys.stdin.readline().strip().split()))
    operations_len = len(operations)
    if operations_len == 2:
        oper, num = operations[0], int(operations[1])
        if oper == 'add':
            if num not in S:
                S.append(num)
        elif oper == 'remove':
            if num in S:
                S.remove(num)
        elif oper == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif oper == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.append(num)
    elif operations_len == 1:
        if operations[0] == 'all':
            S = [i for i in range(1, 21)]
        elif operations[0] == 'empty':
            S = []