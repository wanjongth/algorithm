# 최단경로 - 다익스트라
# 음의 간선이 없을때 동작
# 1. 출발 노드 설정
# 2. 최단 거리 테이블 초기화
# 3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계싼하여 최단 거리 테이블 갱신
# 5. 위 과정에서 3,4번 반복

import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보
graph = [[] for i in range(n+1)]
# 방문 체크
visited = [False] * (n+1)
# 최단 거리 테이블
distance = [INF] * (n+1)

# 간선 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 에서 b로 가는 비용이 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중, 가장 최단거리가 짧은 노드의 번호 반환


def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n -1 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드들 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print('도달불가')
    else:
        print(distance[i])

# 시간복잡도 O(V^2) -> 노드의 개수가 많으면 안됨
