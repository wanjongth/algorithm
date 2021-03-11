# 큰 수의 법칙
# 다양한 로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰수를 만드는 법칙
# 단, 특정 인덱스의 수가 연속해서 K번을 초과하여 더해질 수 없음

# 예) 2, 4, 5, 4, 6 의 배열 -> M = 8, K = 3
#  -> 6 + 6 + 6 + 5 + 6 + 6+ 6 + 5

# 다른 인덱스에 같은 수가 있다면 서로 다른 것으로 간주

# 입력 : 배열의 크기 N, 더해지는 횟수 M, K가 주어진다
#       둘째 줄에 배열이 주어진다
# 예) 5 8 3
# 2 4 5 4 6

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

# print(array)
array.sort(reverse=True)
# print(array)
first = array[0]
# print(first)
second = array[1]
# print(second)

# # 첫번째 답안 - M이 커지면 시간초과
# result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1  # 더할때마다 m 하나씩 빼기
#     if m == 0:
#         break
#     result += second
#     m -= 1  # 더할때마다 m 하나씩 빼기

# print(result)

# # 두번째 답안 - 반복되는 수열 파악
# # M을 K+1로 나눈 몫이 수열이 반복되는 횟수가 됨. 다시 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수
# # 이때 M이 k+1로 나누어 떨어지지 않는 경우 나머지만큼 가장 큰 수가 추가로 더해짐

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
