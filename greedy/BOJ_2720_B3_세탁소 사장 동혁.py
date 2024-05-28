import sys

t = int(sys.stdin.readline())
result = []
n_list = []
for _ in range(t):
    n_list.append(int(sys.stdin.readline()))

for n in n_list:
    print(n//25, end=" ")
    n = n%25
    print(n//10, end=" ")
    n = n%10
    print(n//5, end=" ")
    n = n%5
    print(n//1, end=" ")
    n = n%1
    print()
    