# 미래도시
# 공중 미래 도시에는 1번 부터 N번 까지의 회사가 있는데, 특정 회사끼리는 서로 도로를 통해 연결되어 있음
# 방문 판매원 A는 현재 1번 회사에 위치해 있고, X번 회사에 방문해 물건을 판매하고자 함
# 연결된 2개의 회사는 양방향 이동, 특정회사끼리 연결되어 있다면 정확히 1만큼의 시간으로 이동 가능
# A는 소개팅에도 참석하고자 함. 소개팅 상대는 K번 회사에 존재
# A는 X번 회사에 가서 물건을 판매하기 전에 소개팅 상대의 회사에 찾아가서 커피 마실 예정
# 따라서 A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤 X번 회사로 가는것이 목표
# 최소 시간 계산

# 입력 : 첫째 줄에 전체 회사 개수 N, 경로의 개수 M
# 둘쨰줄 부터 M + 1 번째 줄에는 연결된 두 회사의 번호
# M + 2번째 줄에 X,K

# N의 범위가 100 이하로 매우 한정적이므로 비교적 구현이 간단한 플로이드 워셜 알고리즘으로 해결
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 양방향, 비용 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

# 입력 예
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# 출력 : 3
