import sys

str_list = []
result = ''
max_len = 0

for _ in range(5):
    word = list(map(str, sys.stdin.readline().strip()))
    str_list.append(word)
    max_len = max(max_len, len(word))
    
for i in range(max_len):
    for j in range(5):
        try:
            if str_list[j][i]:
                result += str_list[j][i]
        except Exception as e:
            continue

print(result)