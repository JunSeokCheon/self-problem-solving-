import sys
from collections import defaultdict

student = int(sys.stdin.readline())
stduent_contain = []
ban = defaultdict(list)
student_ban = defaultdict(list)

for _ in range(student):
    stduent_contain.append(list(map(int, sys.stdin.readline().split())))
    
for i in range(5):
    for j in range(student):
        ban[stduent_contain[j][i]].append(j+1)

    for keys, values in ban.items():
        if len(values) > 1:
            for value in values:
                student_ban[value].extend(values)
                student_ban[value] = list(set(student_ban[value]))
    ban = defaultdict(list)

result = sorted(student_ban.items(), key=lambda x: (-len(x[1]), x[0]))
if len(result) != 0:
    print(result[0][0])
else:
    print(1)