import sys

n = int(sys.stdin.readline().strip())
n_list = []
# 계산되었는지 확인 배열
checked = [0] * n
checked_positive = []

for _ in range(n):
    n_list.append(int(sys.stdin.readline().strip()))

n_list.sort()
for i in range(n-1, 0, -1):
    # 현재 값이 0이하의 값이고, 계산이 되어 있지 않으면 n_list 분리
    if n_list[i] <= 0 and checked[i] == 0:
        checked_positive = n_list[i+1:]
        n_list = n_list[:i+1]
        checked = checked[:i+1]
        break

    if checked[i] == 0:
        if n_list[i] * n_list[i-1] > n_list[i] + n_list[i-1]:
            n_list[i] = n_list[i] * n_list[i-1]
            n_list[i-1] = 0
            checked[i-1] = 1

# 현재 n_list에는 0이하의 숫자들만 포함되어 있다.
for i in range(len(n_list)-1):
    # 아직 계산되지 않았다면 로직 처리
    if (checked[i] == 0) and (checked[i+1]==0):
        if n_list[i] * n_list[i+1] > n_list[i] + n_list[i+1]:
            n_list[i] = n_list[i] * n_list[i+1]
            n_list[i+1] = 0
            checked[i+1] = 1

print(sum(checked_positive)+sum(n_list))