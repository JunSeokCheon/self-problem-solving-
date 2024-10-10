import sys
from collections import Counter

word = sys.stdin.readline().strip()
word = word.upper()
result = []

counter_word = Counter(word)
max_cnt = max(counter_word.values())

for keys, values in counter_word.items():
    if values == max_cnt:
        result.append(keys)

if len(result) >= 2:
    print('?')
else:
    print(result[0])