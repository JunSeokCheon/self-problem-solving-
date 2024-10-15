def solution(diffs, times, limit):
    answer = 1
    min_level, max_level = 1, max(diffs)
    
    while min_level < max_level:
        middle_level = (min_level + max_level) // 2
        solved_time = 0
        time_prev = 0
        for diff, time in zip(diffs, times):
            if middle_level >= diff:
                solved_time += time
                time_prev = time
            else:
                incorrect_count = diff - middle_level
                solved_time += ((time+time_prev)*incorrect_count + time)
                time_prev = time
        if solved_time <= limit:
            max_level = middle_level
        else:
            min_level = middle_level + 1

    return min_level