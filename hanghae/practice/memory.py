# # -------------------------------------------------------------------------------------------------
# # queue를 이용한 BFS
#
# import sys
# import collections
#
# nodes = int(sys.stdin.readline())
# edges = collections.defaultdict(list)
# parents = [-1]*2+[0]*(nodes-1)
# queue = collections.deque()
# queue.append(1)
#
# for _ in range(nodes-1):
#     edge = tuple(map(int, sys.stdin.readline().split()))
#     edges[edge[0]].append(edge[1])
#     edges[edge[1]].append(edge[0])
#
# while queue:
#     now = queue.popleft()
#     for kid in edges[now]:
#         if parents[kid] == 0:
#             parents[kid] = now
#             queue.append(kid)
#
# for i in parents[2:]:
#     print(i)
#
#
#
# # -------------------------------------------------------------------------------------------------
# # stack을 이용한 DFS
#
# import sys
# import collections
#
# nodes = int(sys.stdin.readline())
# edges = collections.defaultdict(list)
# parents = [-1]*2+[0]*(nodes-1)
# stack = list()
# stack.append(1)
#
# for _ in range(nodes-1):
#     edge = tuple(map(int, sys.stdin.readline().split()))
#     edges[edge[0]].append(edge[1])
#     edges[edge[1]].append(edge[0])
#
# while stack:
#     now = stack.pop()
#     for kid in edges[now]:
#         if parents[kid] == 0:
#             parents[kid] = now
#             stack.append(kid)
#
# for i in parents[2:]:
#     print(i)



# -------------------------------------------------------------------------------------------------
# 재귀 함수로 풀이

import sys
import collections

# sys.setrecursionlimit(10**7)

nodes = int(sys.stdin.readline())
edges = collections.defaultdict(list)
parents = [-1]*2+[0]*(nodes-1)
queue = collections.deque()

for _ in range(nodes-1):
    edge = tuple(map(int, sys.stdin.readline().split()))
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])


def dfs(node):
    kids = edges[node]
    for kid in kids:
        if parents[kid] == 0:
            parents[kid] = node
            dfs(kid)
    return

dfs(1)

for i in parents[2:]:
    print(i)