def time_convert(time):
    minute, second = map(int, time.split(':'))
    return minute*60+second

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    video_len = time_convert(video_len)
    pos = time_convert(pos)
    op_start = time_convert(op_start)
    op_end = time_convert(op_end)
    
    if op_start <= pos <= op_end:
        pos = op_end
    
    for command in commands:
        if command == 'prev':
            if pos < 10:
                pos = 0
            else:
                pos -= 10
                
            if op_start <= pos <= op_end:
                pos = op_end
        elif command == 'next':
            if video_len - pos < 10:
                pos = video_len
            else:
                pos += 10       
            if op_start <= pos <= op_end:
                pos = op_end
        
    if op_start <= pos <= op_end:
        pos = op_end
    
    minute = str(pos//60)
    second = str(pos%60)
    
    if len(minute) == 1:
        answer += '0' + minute
    else:
        answer += minute
    
    answer += ":"
    
    if len(second) == 1:
        answer += '0' + second
    else:
        answer += second
    
    return answer