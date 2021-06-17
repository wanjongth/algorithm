# 전보
# 어떤 나라에는 N개의 도시가 있다.
# 보내고자하는 메시지가 있는 경우 다른 도시로 전보를 보낸다.
# 통로가 있어야 하고, 메시지를 보낼 때는 일정 시간이 소요된다.
# C라는 도시에서 위급 상황이 발생해, 최대한 많은 도시로 메시지를 보내고자 한다.
# 메시지는 도시 C에서 출발하여, 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
# C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇개이며, 도시들이 모두 메시지를 받게되는 시간을 계산해라

# 입력조건
# 첫째줄 : n,m,c
# 둘째 줄부터 m+1 -> x,y,z(시간)
# 출력조건
# 메시지를 받는 도시의 개수, 총 걸리는 시간

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수, 시작 도시
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
# 최단거리 테이블
distance = [INF] * (n+1)

# 간선 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 자신을 제외하고 카운트, 맥스거리 출력
print(count-1, max_distance)

# 입력 예
# 3 2 1
# 1 2 4
# 1 3 2
# 출력
# 2 4
