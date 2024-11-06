import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())
word_list = []
for _ in range(N):
    word = sys.stdin.readline().strip()
    if len(word) >= M:
        word_list.append(word)

counter_wordList = Counter(word_list)
result = sorted(counter_wordList.items(), key= lambda x : (-x[1], -len(x[0]), x[0]))
for info in result:
    print(info[0])