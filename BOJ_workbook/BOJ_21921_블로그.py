# 시간 초과
# import sys

# N, X = map(int, sys.stdin.readline().split())
# visitor = list(map(int, sys.stdin.readline().split()))
# max_visitor, max_day = 0, 0
# if max(visitor) == 0:
#     print('SAD')
# else:
#     for i in range(0, N-X+1):
#         if sum(visitor[i:i+X]) >= max_visitor:
#             max_visitor = sum(visitor[i:i+X])
    
#     for i in range(0, N-X+1):
#         if sum(visitor[i:i+X]) == max_visitor:
#             max_day += 1
    
#     print(max_visitor)
#     print(max_day)

# 슬라이딩 윈도우 기법 -> 한 칸씩 가면서 맨 앞 값 빼주고, 그 다음값 더해주고 반복
import sys

N, X = map(int, sys.stdin.readline().split())
visitor = list(map(int, sys.stdin.readline().split()))
visitor_sum, max_day = sum(visitor[:X]), 1
if max(visitor) == 0:
    print('SAD')
else:
    max_visitor = visitor_sum
    for i in range(X, N):
        visitor_sum -= visitor[i-X]
        visitor_sum += visitor[i]
        
        if visitor_sum > max_visitor:
            max_visitor = visitor_sum
            max_day = 1
        elif max_visitor == visitor_sum:
            max_day += 1
    
    print(max_visitor)
    print(max_day)