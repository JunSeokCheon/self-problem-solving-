import sys

n, c = map(int, sys.stdin.readline().split())
coorp = []
result = []
for _ in range(n):
    num = int(sys.stdin.readline())
    coorp.append(num)

coorp.sort()
start = 1
end = coorp[-1] - coorp[0]

while start <= end:
    middle = (start + end) // 2
    cur = coorp[0]
    cnt = 1
    
    for i in range(1, len(coorp)):
        if coorp[i] >= cur + middle:
            cur = coorp[i]
            cnt += 1
    
    if cnt < c:
        end = middle - 1
    elif cnt >= c:
        start = middle + 1

print(end)
    