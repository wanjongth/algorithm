from collections import deque
graph = {}
n, m, v = map(int, input().split())
for i in range(n):
    graph[i+1] = []
for i in range(m):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]
start_node = v


def dfs_stack(graph, start_node):
    stack = [start_node]
    visited = []
    while stack:
        log = stack.pop()
        if log not in visited:
            print(log, end=' ')
        graph[log].sort(reverse=True)
        visited.append(log)
        for i in graph[log]:
            if i not in visited:
                stack.append(i)


def bfs_queue(graph, start_node):
    queue = deque()
    queue.append(start_node)
    visited = []
    while queue:
        log = queue.popleft()
        if log not in visited:
            print(log, end=' ')
        graph[log].sort()
        visited.append(log)
        for i in graph[log]:
            if i not in visited:
                queue.append(i)


dfs_stack(graph, start_node)
print()
bfs_queue(graph, start_node)
