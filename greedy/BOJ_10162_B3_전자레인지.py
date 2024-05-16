import sys

time = int(sys.stdin.readline())
btn = [300, 60, 10]
result = []

for bt in btn:
    if time//bt > 0:
        result.append(time//bt)
    else:
        result.append(0)
    time = time % bt

if time > 0:
    print(-1)
else:
    print(*result)