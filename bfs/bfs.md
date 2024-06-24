# BFS (Breadth First Search)
- 너비 우선 탐색이라고 부르며, 가까운 노트부터 탐색하는 알고리즘
- 가장 가까운 노드부터 우선 순위를 가지기 때문에, 큐(Queue)를 이용하여 구현할 수 있다.
- Python에서는 depue 라이브러리를 통해 큐를 사용할 수 있다.
- 일반적으로 DFS보다 수행 시간이 좋은 편이다.

## 동작과정
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복

```python
from collections import deque

# BFS
def BFS(graph, start, visited):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque([start])

  # 현재 노드 방문 처리
  visited[start] = True

  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end = ' ')

    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True



visited =[False] * 9

# 각 노드가 연결된  정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
  [],                 # 1번 노드와 연결된 노드들
  [2, 3, 8],          # 2번 노드와 연결된 노드들
  [1, 7],             # 3번 노드와 연결된 노드들
  [1, 4, 5],          # 4번 노드와 연결된 노드들
  [3, 5],             # 5번 노드와 연결된 노드들
  [3, 4],             # 6번 노드와 연결된 노드들
  [7],                # 7번 노드와 연결된 노드들
  [2, 6, 8],          # 8번 노드와 연결된 노드들
  [1, 7]              # 9번 노드와 연결된 노드들
]

BFS(graph, 1, visited)

# 결과
1 2 3 8 7 4 5 6
```
