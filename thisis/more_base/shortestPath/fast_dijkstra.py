# 개선된 다익스트라
# 힙 사용 -> 우선순위 큐
# 파이썬 -> PriorityQueue or heapq 사용
# (가치, 물건)으로 묶어 우선순위 큐 자료구조에 넣음
# 가치값이 우선순위, 보통 첫번째 원소 기준
#
# 최단 거리 테이블을 그대로 사용하며 가장 가까운 노드를 저장하기 위한 우선순위 큐(최소 힙)사용

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블
distance = [INF] * (n+1)

# 모든 간선 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 처리된 적 있다면 무시
        if distance[now] < dist:
            continue
        # 인접한 다른 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("도달불가")
    else:
        print(distance[i])

# 시간 복잡도 -> O(ElogV)

# 입력 예
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
