#         1
#     2   5   9
#    3   6 8  10
#   4   7


# graph = {
#     1: [2, 5, 9],
#     2: [1, 3],
#     3: [2, 4],
#     4: [3],
#     5: [1, 6, 8],
#     6: [5, 7],
#     7: [6],
#     8: [5],
#     9: [1, 10],
#     10: [9]
# }
# visited = []

# # 재귀함수, DFS의 깊이가 무한정 깊어지면 에러가 발생

# def dfs_recursion(adjacent_graph, cur_node, visited_array):
#     visited_array.append(cur_node)
#     for adjacent_node in adjacent_graph:
#         if adjacent_node not in visited_array:
#             dfs_recursion(adjacent_graph, adjacent_node, visited_array)
#     return


# dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
# print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!


# 다른방법 - 스택
# 인접한 노드 중 방문하지 않은 모든 노드들을 저장해두고, 가장 마지막에 넣은 노드들만 꺼내서 탐색
# 방문하지 않았다는 조건을 표시하기 위해 visited 배열에 기록

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# 1. 시작 노드를 스택에 넣습니다.
# 2. 현재 스택의 노드를 빼서 visited 에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중에서 방문하지 않은 노드를 스택에 추가합니다.


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []

    while stack:
        current_node = stack.pop()
        visited.append(current_node)  # [1]
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)

    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!
