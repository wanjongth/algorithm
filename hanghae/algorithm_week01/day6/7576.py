from collections import deque


M, N = map(int, input().split())
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))
# print(box)

queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j])  # 이미 익어있는 토마토 위치를 큐에 넣어줌

while queue:
    [i, j] = queue.popleft()  # 하나씩 빼면서 비교

    # 위
    if i > 0 and box[i-1][j] == 0:
        queue.append([i-1, j])  # 큐에 넣고
        box[i-1][j] = box[i][j] + 1  # 하루 더 기다려야하니, 1을 더해준다.

    # 아래
    if i < N-1 and box[i+1][j] == 0:
        queue.append([i+1, j])
        box[i+1][j] = box[i][j] + 1

    # 왼쪽
    if j > 0 and box[i][j-1] == 0:
        queue.append([i, j-1])
        box[i][j-1] = box[i][j] + 1

    # 오른쪽
    if j < M-1 and box[i][j+1] == 0:
        queue.append([i, j+1])
        box[i][j+1] = box[i][j] + 1

answer = True


for row in box:  # 0이 하나라도 있을 경우 -1출력
    if 0 in row:
        print(-1)
        answer = False
        break

print(box)

if answer:
    min_day = 0
    for row in box:
        min_day = max(min_day, max(row))  # 익기 위한 최소 날 = box 최댓값
    print(min_day-1)
