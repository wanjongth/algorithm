# N Queen - 백트레킹

# N*N 인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# N이 주어졌을 때 퀸 놓는 방법의 수

# 입력:N, 출력: 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수

n = int(input())


# 퀸과 대각선 혹은 열에 만나는 것이 있는지 확인
col = [0 for _ in range(n)]  # 열 나오는 수 : 0~4 5개(n)
slash = [0 for _ in range(2 * n - 1)]  # 내려가는 대각선 나오는 수 : 0~8 = 9개(2n-1)
backslash = [0 for _ in range(2 * n - 1)]  # 올라가는 대각선 나오는 수 : 0~8 = 9개(2n-1)


def n_queen(k):  # k : 행
    global cnt
    if k == n:  # 종료조건
        cnt += 1  # 돌아온 횟수만큼 출력(경우의 수)
        return

    for i in range(n):
        if not (col[i] or slash[i+k] or backslash[k-i+n-1]):  # 열,대각선에 만나지 않으면
            col[i] = 1  # col i = i번째 행에서 퀸이 놓여있는 열 위치
            slash[i+k] = 1
            backslash[k-i+n-1] = 1
            # print(col, slash, backslash)
            n_queen(k+1)
            col[i] = 0
            slash[i+k] = 0
            backslash[k-i+n-1] = 0


cnt = 0

n_queen(0)
print(cnt)
