# 1이 될때까지 - 그리디
# 어떠한 수 N이 1이 될때까지 두 과정중 하나를 반복적으로 선택하여 수행
# N에서 1을 뺀다
# N을 K로 나눈다. - 나누어 떨어질 때만

# N과 K가 주어질 때 N이 1이 될떄까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수

# 입력: 첫째줄에 N,K(공백), N>K
# 출력: 최솟값

# # 내가 푼 단순한 방법
# n, k = map(int, input().split())

# result = 0

# while n > 1:
#     if not n % k == 0:
#         n -= 1
#         result += 1
#     n = n // k
#     result += 1
# print(result)

# 입력이 커지면 N이 K의 배수가 되도록 효울적으로 한번에 빼는 방식이 있다.
n, k = map(int, input().split())
result = 0

while True:
    # N == K 로 나누어떨어지는 수가 될때까지 1씩 빼기
    target = (n//k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나눔
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
