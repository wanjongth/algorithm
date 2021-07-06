# 거스름돈 - dp - 12907
# Finn은 편의점에서 야간 아르바이트를 하고 있습니다.
# 야간에 손님이 너무 없어 심심한 Finn은 손님들께 거스름돈을 n 원을 줄 때 방법의 경우의 수를 구하기로 하였습니다.
# 거슬러 줘야 하는 금액 n과 Finn이 현재 보유하고 있는 돈의 종류 money가 매개변수로 주어질 때, Finn이 n 원을 거슬러 줄 방법의 수를 return 하도록 solution 함수를 완성해 주세요.

def solution(n, money):
    dp = [1] + [0] * n
    # print(dp)
    for coin in money:
        for price in range(coin, n + 1):
            if price >= coin:
                dp[price] += dp[price - coin] % 100000007

    # print(dp)
    return dp[n]


print(solution(5, [1, 2, 5]))
