from collections import Counter

def solution(points, routes):
    answer = 0
    mini_path = []
    
    for route in routes:
        time = 0
        for i in range(len(route)-1):
            start_x, start_y = points[route[i]-1]
            end_x, end_y = points[route[i+1]-1]
            
            while start_x != end_x:
                mini_path.append((start_x, start_y, time))
                if start_x > end_x:
                    start_x -= 1
                elif start_x < end_x:
                    start_x += 1
                time +=1
            
            while start_y != end_y:
                mini_path.append((start_x, start_y, time))
                if start_y > end_y:
                    start_y -= 1
                elif start_y < end_y:
                    start_y += 1
                time += 1
            
        mini_path.append((start_x, start_y, time))

    for value in Counter(mini_path).values():
        if value >= 2:
            answer += 1
    
    return answer