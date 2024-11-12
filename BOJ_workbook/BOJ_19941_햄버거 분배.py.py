import sys

n, k = map(int, sys.stdin.readline().split())
string_list = list(sys.stdin.readline().strip())
answer = 0

for i in range(len(string_list)):
    if string_list[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1,n)):
            if string_list[j] == "H":
                string_list[j] = 0
                answer += 1
                break

print(answer)
