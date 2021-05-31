# 개미 전사
# 식량 창고 털기 -> 인접한 식량창고는 털지 못한다
# 여기서 최댓값을 구하여라

# 입력 -> 첫째 줄: 식량 창고의 개수 N
#        둘째 줄: 공백으로 구분되어 식량 창고에 저장된 식량의 개수 K
# 출력 -> 식량의 최댓값

# 아이디어
# 인접한 식량 창고는 털지 못하므로
# 1. i - 1 번째 식량창고를 털기로 하면 현재의 식량창고는 털 수 없다
# 2. i - 2 번째 식량창고를 털기로 하면 현재의 식량창고는 털 수 있다
# 1,2 중에 최댓값을 선택한다 ->

# 4
# 1 3 1 5

n = int(input())
k = list(map(int, input().split()))

dp = [0]*100  # n의 범위 만큼 초기화

dp[0] = k[0]
dp[1] = max(k[0], k[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + k[i])

print(dp[n-1])
