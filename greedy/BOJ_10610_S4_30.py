import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int, str(n)))

if (sum(n_list)%3 == 0) and (0 in n_list):
    n_list.sort(reverse=True)
    result = "".join(map(str,n_list))
    print(result)
else:
    print(-1)