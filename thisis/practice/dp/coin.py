# 효율적인 화폐 구성
# N가지 종류의 화폐, 최소한으로 이용해서 가치의 합이 M원이 되도록 함
# 입력 : N, M
# 이후 N개 줄에 화폐의 가치
# 출력 : M원을 만들기 위한 최소 화폐 개수
# 못만들면 -1
# 화폐 구성에서 큰 단위가 작은 단위의 배수가 아니기 때문에 dp
# 적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾으면 됨
# 나올 수 없는 값으로 dp 테이블 초기화,
# 나올 수 있는 값은 화폐 단위에 따른 갱신
# -> min(func[i], func[i-k]+1)

n, m = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

# 초기화
dp = [10001] * (m+1)

dp[0] = 0
for i in range(n):
    for j in range(coin[i], m + 1):
        if dp[j - coin[i]] != 10001:
            dp[j] = min(dp[j], dp[j - coin[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
