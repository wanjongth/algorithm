import sys

n = int(input())

dp = [[0 for _ in range(3)] for _ in range(n)]
# print(dp)

for i in range(n):
    dp[i] = list(map(int, sys.stdin.readline().split()))
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    # i번째 집을 빨간색으로 칠했을 때는 i-1 집이 초록,파랑에서 최솟값으로 칠해야 하고,
    # 최솟값과 빨간색칠 한 값을 더함
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    # i번째 집을 초록색으로 칠했을 때는 i-1 집이 빨강,파랑에서 최솟값으로 칠해야 하고,
    # 최솟값과 초록색칠 한 값을 더함
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]
    # i번째 집을 파랑색으로 칠했을 때는 i-1 집이 빨강,초록에서 최솟값으로 칠해야 히고,
    # 최솟값과 파랑색칠 한 값을 더함

print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))
