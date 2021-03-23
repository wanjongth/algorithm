# 상하좌우 - 시뮬레이션

# 시작좌표 (1,1), N*N 정사각형 공간에서 움직이는 프로그램
# 계획서가 주어졌을 때 최족적으로 도착할 지점의 좌표 출력

# 입력 - 첫째줄 : 공간의 크기 N, 둘째줄 : 이동할 계획 내용
# 출력 - 도착 지점의 좌표를 공백으로 구분하여 출력

n = int(input())
x, y = 1, 1
plans = list(input().split())

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]  # L : (0,-1) R : (0,1) U : (-1,0), D : (1,0)
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue  # 무시하고 진행
    # 좌표 변화
    x, y = nx, ny

print(x, y)
