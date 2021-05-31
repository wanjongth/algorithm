# 1로 만들기
# 정수 X에 사용할 수 있는 연산은 4가지
# X가 5로 나누어 떨어지면 5로 나눔
# X가 3으로 나누어 떨어지면 3으로 나눔
# X가 2로 나누어 떨어지면 2로 나눔
# X에서 1을 뺀다

# 입력 : 정수 x
# 출력 : 연산을 하는 최솟값

x = int(input())

# 계산된 결과를 저장하기 위한 dp 테이블
dp = [0] * 30001

# dp bottom up
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[x])
