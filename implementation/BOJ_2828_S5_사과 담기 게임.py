import sys

n, m = map(int, sys.stdin.readline().split())
j = int(sys.stdin.readline())
j_list = [int(sys.stdin.readline()) for _ in range(j)]
now = 1
answer = 0

for apple in j_list:
    if now <= apple and now + (m-1) >= apple:
        pass
    elif now > apple:
       answer += abs(apple - now)
       now = apple
    else:
        answer += apple - (m-1) - now
        now = apple - (m-1)
print(answer) 