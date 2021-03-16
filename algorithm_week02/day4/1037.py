# 약수 - 정수론 및 조합론
# 진짜 약수
# 1과 N이 아닌 어떤 수 N의 진짜 약수가 주어질 때 N을 구하는 프로그램

# 입력 : 첫째 줄에 N의 약수의 개수, 둘째 줄에 N의 진짜 약수
# 출력 : N

# 약수를 1부터 조금 써보면
# 20 - 2 4 5 10
# 100 - 2 4 5 10 20 25 50
# 문제에서 1과 자기 자신을 빼고 약수들이 나와있는데
# 리스트의 첫번째 원소와 마지막 원소를 곱해주면 그 값이 나온다
# 혹시 몰라서 sort함
n = int(input())
array = list(map(int, input().split()))
array.sort()
result = array[0] * array[-1]
print(result)

# # 방법2
# # max()와 min()을 사용한다.
# import sys
# input = sys.stdin.readline

# n = int(input()) # 3 / 약수 개수
# divisor = list(map(int, input().split())) # [8,4,2] / 진짜 약수들 (1과, N은 제외)

# # 가장 큰 값 * 가장 작은 값 = N
# # divisor.sort() <- 입력 조건이 이상하게 들어올 경우를 고려해서 정렬해준다.
# # print(divisor[0]*divisor[-1])

# d_max = max(divisor)
# d_min = min(divisor)
# print(d_max * d_min)
