# 만들 수 없는 금액
# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램

# 입력 :
# 첫째 줄에는 동전의 개수 N
# 둘째줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수
# 출력 : 만들 수 없는 최소 금액

n = int(input())
coin = list(map(int, input().split()))

coin.sort()

target = 1
for i in coin:
    if target < i:
        break
    target += i

print(target)
