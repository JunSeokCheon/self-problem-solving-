# python round 함수의 문제점 : 0.5의 경우 0이랑 0.5 차이가 나고, 1이랑 0.5 차이가 난다.
# 위의 경우, 앞 수가 짝수면 버려지고, 홀수면 올림이 된다. ex. 0.5 -> 0, 1.5 -> 2
# 해결 - 사사오입 방법 사용 : 결과에 영향을 끼치지 않은 아주 작은 값을 더함으로써 반올림을 확실하게 만듬
import sys

n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for _ in range(n)]
EPS = 1e-9

if n == 0:
    print(0)
else:
    cut_avg = round(n*0.15 + EPS)
    n_list.sort()
    cal_list = n_list[cut_avg:n-cut_avg]
    print(round(sum(cal_list)/len(cal_list) + EPS))