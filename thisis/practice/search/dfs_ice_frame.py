# 음료수 얼려 먹기
# n*m 크기의 얼음 틀이 있을때, 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시
# 구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어있는 경우 서로 연결되어 있는 것으로 간주한다.
# 아이스크림의 개수를 구하여라

# 입력 : 첫째 줄  - n,m
# 두 번째 줄부터 N + 1 번째 줄까지 얼음틀의 형태가 주어진다.
# 입력 예
# 4 5
# 00110
# 00011
# 11111
# 00000

# 특정한 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에 값이 0이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
# 방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문 가능
# 위의 과정을 모든 노드에 반복 수행


# 출력 : 한 번에 만들 수 있는 아이스크림의 개수
n, m = map(int, input().split())

graph = list()
for _ in range(n):
    graph.append(list(map(int, input())))

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드에 대해 수행하면서 수 세기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
