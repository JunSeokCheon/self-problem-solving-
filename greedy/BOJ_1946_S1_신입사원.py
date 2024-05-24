# 틀림
# import sys

# t = int(sys.stdin.readline().strip())
# for _ in range(t):
#     result_idx_list = []
#     n = int(sys.stdin.readline().strip())
#     n_list = []
#     for _ in range(n):
#         w, i = map(int, sys.stdin.readline().strip().split())
#         n_list.append([w,i])
#     sorted_w = sorted(n_list, key = lambda x: x[0])
#     sorted_i = sorted(n_list, key = lambda x: x[1])
#     i_standard = sorted_i[0][0]
#     w_standard = sorted_w[0][1]
    
#     for idx, wi in enumerate(n_list):
#         x, y = wi[0], wi[1]
#         if i_standard < x:
#             result_idx_list.append(idx)
        
#         if w_standard < y:
#             result_idx_list.append(idx)
    
#     print(len(n_list) - len(set(result_idx_list)))

import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    N_list = []
    result = 0
    for _ in range(N):
        resume, interview = map(int, sys.stdin.readline().strip().split())
        N_list.append([resume, interview])
    N_list = sorted(N_list, key = lambda x : x[0])
    
    compare_interview_score = N_list[0][1]
    for i in range(len(N_list)):
        if compare_interview_score >= N_list[i][1]:
            result += 1
            compare_interview_score = N_list[i][1]
    print(result)