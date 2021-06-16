# 바닥공사
# 가로 N, 세로 2인 직사각형 얇은 바닥
# 1*2 덮개, 2*1 덮개, 2*2 덮개를 이용해 채우려고함
# -> 초기값 n = 1 : 1, n = 2 : 3
# 점화식 : func[i] = func[i-1] + 2 * func[i-2]
def solution(n):
    # dp 테이블 초기화
    dp = [0]*1001
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + 2 * dp[i-2]) % 796796

    return dp[n]


print(solution(3))
