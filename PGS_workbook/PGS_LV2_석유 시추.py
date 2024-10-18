from collections import deque
import copy

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

group = {}

def bfs(row, col, visited, land, group_num):
    que = deque()
    que.append((row, col))
    visited[row][col] = group_num
    count = 1
    
    while que:
        x, y = que.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx < 0 or nx >= len(land) or ny < 0 or ny >= len(land[0]):
                continue
            
            if land[nx][ny] == 1 and visited[nx][ny] == -1:
                que.append((nx,ny))
                count += 1
                visited[nx][ny] = group_num

    group[group_num] = count
    
def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    visited = [[-1]*(m) for _ in range(n)]
    group_num = 0
    
    for row in range(n):
        for col in range(m):
            if visited[row][col] == -1 and land[row][col] == 1:
                bfs(row, col, visited, land, group_num)
                group_num += 1
    
    for i in range(m):
        group_list = []
        result = 0
        for j in range(n):
            if land[j][i] == 1 and visited[j][i] not in group_list:
                group_number = visited[j][i]
                result += group[group_number]
                group_list.append(group_number)
        answer = max(answer, result)
                
    return answer