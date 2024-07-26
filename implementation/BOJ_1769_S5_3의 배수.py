import sys

X = list(map(int, sys.stdin.readline().strip()))
X_sum = sum(X)
result = 1

while X_sum > 9:
    X_sum_str = str(X_sum)
    X_sum = sum(list(map(int, X_sum_str)))
    result += 1

if len(X) < 2:
    print(0)
else:
    print(result)
if X_sum % 3 == 0:
    print("YES")
else:
    print("NO")