import sys, heapq

N, score, P = map(int, sys.stdin.readline().split())
result = 1

if N == 0:
    print(1)
else:
    ranking = list(map(int, sys.stdin.readline().split()))
    if N == P and ranking[-1] >= score:
        print(-1)
    else:
        heap = []
        for rank in ranking:
            heapq.heappush(heap, -rank)
        heapq.heappush(heap, -score)
        
        temp_value = 0
        mini_rank = 0
        for _ in range(len(heap)):
            num = -heapq.heappop(heap)
            if num == score:
                print(mini_rank+ result)
                break
            else:
                if temp_value == num:
                    mini_rank += 1
                else:
                    temp_value = num
                    mini_rank += 1
                
                