# 플로이드 워셜 알고리즘
# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
# O(N^3)
# 최단경로 + dp

INF = int(1e9)

n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고 모든 값 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신은 비용 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선의 정보 입력받아 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우
        if graph[a][b] == INF:
            print("도달 불가")
        else:
            print(graph[a][b], end=" ")
    print()

# 입력 예
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
