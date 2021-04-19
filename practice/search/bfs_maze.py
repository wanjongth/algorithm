# 미로탈출 - bfs
# N*M 크기의 직사각형 형태의 미로에서, 여러 마리의 괴물을 피해 탈출해야 함
# 처음 위치는 (1,1)이고 미로의 출구는 (n,m)의 위치에 존재하며 한번에 한 칸씩 이동
# 괴물이 있는 부분은 0, 없는 부분은 1로 표시
# 탈출하기 위해 움직여야 하는 최소 칸의 개수(칸을 셀 때는 시작,마지막 칸을 모두 포함해서 계산)

# 입력 : 첫째 줄 - n, m 둘째 줄부터 N개의 줄에는 m개의 정수로 미로의 정보
# 출력 : 최소 이동 칸의 개수
# 입력 예
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

n, m = map(int, input().split())

graph = list()
for _ in range(n):
    graph.append(list(map(int, input())))

# 네 방향 정의(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 네 방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 처음 방문하는 경우 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]


print(bfs(0, 0))
