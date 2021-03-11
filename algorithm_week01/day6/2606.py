n = int(input())
link = int(input())
# 노드의 개수 = n
# 간선의 개수 = link
# 각 간선의 양 끝 노드

# 주어진 변수로 인접 리스트 만들기
dic = {}  # 딕셔너리 초기화
for i in range(n):
    dic[i+1] = list()  # 노드:[] 형식 - 1부터 n까지
# print(dic)
for j in range(link):  # 간선의 개수만큼 데이터 추가해주기
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

# print(dic)


def dfs(start, graph):
    stack = [start]
    visited = []

    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        for adj_node in graph[current_node]:
            if adj_node not in visited:
                stack.append(adj_node)
    visited = set(visited)

    return list(visited)


def bfs_queue(start, graph):
    queue = [start]
    visited = []

    while queue:  # 큐가 비지 않는 동안
        current_node = queue.pop(0)  # 0번째 원소 뽑기
        visited.append(current_node)
        for adj_node in graph[current_node]:
            if adj_node not in visited:
                queue.append(adj_node)
    visited = set(visited)
    return list(visited)


# print(len(dfs(1, dic)) - 1)
# print(len(bfs_queue(1, dic)) - 1)
