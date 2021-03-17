# DFS와 BPS

# 그래프를 DFS로 탐색한 결과, BFS로 탐색한 결과를 출력
# 정점이 여러 개인 경우는 정점 번호가 작은 것을 먼저 방문, 더 이상 방문할 수 있는 점이 없는 경우 종료

# 입력 : 첫째줄 - 정점의 개수 N, 간선의 개수 M, 탐색 시작할 정점 번호 V
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호
# 어떤 두 정점 사이에 여러 개의 간선, 간선은 양방향

# 출력: 첫째줄 : DFS, 둘째줄 : BFS

# # dfs 스택 - 리스트에 넣을때 방문표시 해주고 print 해줘야하는데 방법을 모르겠음.. dfs 는 일단 재귀
# def dfs(v):
#     stack = [v]  # 시작 노드를 리스트에 넣어준다
#     visit[v] = 1  # 시작 노드를 방문표시 해준다
#     while stack:  # 스택이 비지 않을 동안에
#         v = stack.pop()  # 스택에서 제거하고
#         print(v, end=' ')  # 프린트
#         for node in range(1, n + 1):  # node를 돌면서
#             if visit[node] == 0 and graph[v][node] == 1:  # 만약 그 노드를 방문하지 않았고, 연결되어 있다면
#                 stack.append(node)  # 노드를 스택에 넣어준다
#                 visit[node] = 1  # 방문표시 해준다

# # 억지로 짜맞춘 코드인데 테스트케이스는 통과, 제출 시 틀렸다고 나옴
# def dfs(v):
#     stack = [v]
#     visit[v] = 1
#     while stack:
#         v = stack.pop()
#         print(v, end=' ')
#         for i in range(1, n + 1):
#             if visit[i] == 0 and graph[v][i] == 1:
#                 stack.append(i)
#                 visit[i] = 1
#                 break


from collections import deque

# # dfs 재귀


# def dfs(v):
#     print(v, end=' ')  # 현재 v 값을 출력한다
#     visit[v] = 1  # 방문 리스트에 방문표시(1)을 해준다.
#     for node in range(1, n + 1):  # 각 노드들을 돌면서(1~n까지의 노드)
#         if visit[node] == 0 and graph[v][node] == 1:  # 방문하지 않았고 그 node와 연결되어있다면
#             dfs(node)  # 다시 dfs(node)를 부른다


def bfs(v):
    queue = deque([v])  # 덱사용, 시작노드를 덱에 넣어준다.
    visit[v] = 1  # 시작노드를 방문표시 해준다
    while queue:  # 큐가 비지 않을 동안
        v = queue.popleft()  # 큐에서 빼고
        print(v, end=' ')  # 프린트
        for node in range(1, n + 1):  # node를 돌면서
            if visit[node] == 0 and graph[v][node] == 1:  # 만약 그노드를 방문하지 않았고, 연결되어 있다면
                queue.append(node)  # 노드를 큐에 넣어준다
                visit[node] = 1  # 방문표시를 해준다.


n, m, v = map(int, input().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]  # n+1 * n+1 크기의 2차원 배열
# print(graph)
visit = [0 for i in range(n+1)]  # 방문 표시할 것 0으로 초기화
# print(visit)
for _ in range(m):
    x, y = map(int, input().split())  # x,y 값을 받아와서
    graph[x][y] = graph[y][x] = 1  # 그래프에 표시해준다
# print(graph)
dfs(v)
# print(visit)
print()
visit = [0 for i in range(n+1)]  # dfs를 갔다오면 방문기록이 남으므로 초기화
bfs(v)
