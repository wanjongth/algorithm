import math

# # case1) 나누어 떨어지면 그 숫자는 소수가 아님.

# def sosu(x):
#     if x == 1:
#         return False
#     else:
#         for i in range(2, int(math.sqrt(x)+1)):  # 2 ~ 제곱근까지만 판별
#             # for i in range(2, int(x**0.5)+1):
#             if x % i == 0:
#                 return False
#         return True


# A, B = map(int, input().split())

# for j in range(A, B+1):  # A~B까지
#     if sosu(j):
#         print(j)


# # case2) 계속 시간초과 : 최대공약수는 안되나 ??;
# def sosu2(x):
#     if x == 1:
#         return False
#     else:
#         for i in range(2, int(math.sqrt(x)+1)):
#             if math.gcd(i, x) != 1:
#                 return False
#         return True


# A, B = map(int, input().split())

# for j in range(A, B+1):
#     if sosu2(j):
#         print(j)


# # 에라토스테네스의 체 - 위보다 빠름

# m, n = map(int, input().split())
# array = [True for i in range(1000001)]  # 모든 수가 소수인것으로 초기화
# array[1] = 0  # 1은 소수가 아님

# # 에라토스테네스의 체
# for i in range(2, int(math.sqrt(n)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인
#     if array[i] == True:  # i 가 소수인경우
#         # i를 제외한 i의 모든 배수 제거
#         # j = i ..
#         j = 2
#         while i * j <= n:
#             array[i*j] = False
#             j += 1

# # M부터 N까지의 모든 소수 출력
# for i in range(m, n+1):
#     if array[i]:
#         print(i)


# 위와 같으나 for문 표현이 다름
m, n = map(int, input().split())


def sosu(m, n):
    n += 1
    array = [True] * n  # 모두 소수
    for i in range(2, int(n**0.5)+1):
        if array[i]:
            for j in range(2*i, n, i):
                array[j] = False

    for i in range(m, n):
        if i > 1 and array[i] == True:
            print(i)


sosu(m, n)
