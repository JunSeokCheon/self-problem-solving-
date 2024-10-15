from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    que1_sum = sum(queue1)
    que2_sum = sum(queue2)
    
    half_sum = (que1_sum + que2_sum) // 2
    
    for i in range(1, len(queue1)*4):
        if que1_sum > half_sum:
            pop_num = queue1.popleft()
            queue2.append(pop_num)
            que1_sum -= pop_num
            que2_sum += pop_num
        elif que2_sum > half_sum:
            pop_num = queue2.popleft()
            queue1.append(pop_num)
            que2_sum -= pop_num
            que1_sum += pop_num
        else:
            return i-1
    
    return -1
    