# 너비 우선 탐색
# 최대한 가까이 있는 노드들을 우선으로 탐색
# 선입선출 방식인 큐 자료구조를 이용

# 동작방식
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복

# 추가 메모 : 2차원 배열에서의 탐색 문제를 만나면 그래프 형태로 바꿔서 생각하면 풀이 방법을 좀 더 쉽게 떠올릴 수 있다.

from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된 아직 방문하지 않은 원소들 큐에 삽입하고 방문처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
