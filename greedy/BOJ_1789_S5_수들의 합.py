import sys

s = int(sys.stdin.readline())

result = 0
num = 1

while True:
    if s >= num:
        s -= num
        num += 1
        result += 1
    else:
        print(result)
        break