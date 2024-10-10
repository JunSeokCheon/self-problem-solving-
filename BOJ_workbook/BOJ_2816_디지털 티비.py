import sys

N = int(sys.stdin.readline())
channels = [sys.stdin.readline().strip() for _ in range(N)]
result = ''

cur = 0
for i in range(len(channels)):
    if channels[i] == 'KBS1':
        break
    cur += 1

result += '1'*cur
result += '4'*cur

channels.remove('KBS1')
channels = ['KBS1'] + channels

cur = 0
for i in range(len(channels)):
    if channels[i] == 'KBS2':
        break
    cur += 1
    
result += '1'*cur
result += '4'*(cur-1)

print(result)