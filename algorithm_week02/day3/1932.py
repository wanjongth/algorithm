# 정수삼각형
# 맨 위층부터 아래에 있는 수 중 하나를 선택하여 아래층으로 내려옴
# 제일 아래층에서 선택된 수의 합이 최대가 되는 경로

# 합이 최대가 되는 경로에 있는 수의 합을 출력
import sys
n = int(input())

a = 0
for i in range(1, n+1):
    a += i

dp = [0]*n
for i in range(n):
    dp[i] = list(map(int, sys.stdin.readline().split()))
# print(dp)


k = 2
for i in range(1, n):
    for j in range(k):  # 리스트 안에 리스트 확장
        # for j in range(i+1):
        if j == 0:  # 맨 왼쪽 숫자
            dp[i][j] = dp[i - 1][j] + dp[i][j]
        elif i == j:  # 맨 오른쪽 숫자
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + dp[i][j]
    k += 1
print(max(dp[n - 1]))


# import sys
# n = int(input())

# a = 0
# for i in range(1, n+1):
#     a += i

# dp = [0]*n

# for i in range(n):
#     dp[i] = list(map(int, sys.stdin.readline().split()))

# result = 0
# for _ in dp:
#     result = result + max(dp[i])
# print(result)
