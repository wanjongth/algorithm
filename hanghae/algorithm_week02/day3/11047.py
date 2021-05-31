# 그리디 - 동전0
# 동전을 적절히 사용하여 가치의 합을 K로, 이때 필요한 동전의 개수 최솟값

# 입력 : 첫째줄 - N, K 둘째줄 - N개의 줄에 동전의 가치 오름차순
import sys

n, k = map(int, sys.stdin.readline().split())

coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)  # 최솟값의 경우이므로 동전의 가치가 큰 순서로 변환
# print(coin)
result = 0
for coin in coins:
    result = result + k // coin  # result에 k를 coin으로 나눈 몫 더함
    k = k % coin  # k를 coin으로 나눈 나머지를 다시 k에 저장

print(result)

# 동전의 종류가 배수가 아니면 사용할 수 없음!
# 만약 K = 800원,
# 동전의 종류 500원, 400원, 100원 인 경우!
