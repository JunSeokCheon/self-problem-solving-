import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
standard = sequence[0]
result = 1
result_list = []

# 연속해서 커지는 경우
for i in range(1, len(sequence)):
    if sequence[i] >= standard:
        result += 1
        standard = sequence[i]
    else:
        result = 1
        standard = sequence[i]
    
    result_list.append(result)

standard = sequence[0]
result = 1

# 연속해서 작아지는 경우
for i in range(1, len(sequence)):
    if sequence[i] <= standard:
        result += 1
        standard = sequence[i]
    else:
        result = 1
        standard = sequence[i]
    
    result_list.append(result)

if result_list:
    print(max(result_list))
else:
    print(1)