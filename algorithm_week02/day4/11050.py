# 이항계수 - 정수론 및 조합론
# 이항계수 - nCk
# 0<=k<=n 일 때, n!/k!(n-k)!
# k<0, k>n 일 때, 0

# 입력 : n과 k , 출력: nCk

# 방법1: math.factorial 활용
import math

n, k = map(int, input().split())

# 입력 조건에 0<=k<=n 이 있지만 다른데서 쓸 수도 있어서 조건 만들어줌


def Combination(n, k):
    if 0 <= k <= n:
        com = math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
        return int(com)
    else:
        return 0


print(Combination(n, k))

# # 방법2 factorial 만들기

# def fac(n):
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#     return result


# n, k = map(int, input().split())


# def Combination(n, k):
#     if 0 <= k <= n:
#         com = fac(n) / (fac(k)*fac(n-k))
#         return int(com)
#     else:
#         return 0


# print(Combination(n, k))


# 방법3 - 재귀 이므로 메모이제이션 이용
# import sys
# input = sys.stdin.readline

# memo = {}

# def factorial(a, fac_memo):
#     if a == 0: # 0! = 1
#         return 1

#     if a == 1:
#         return 1

#     if a in fac_memo:
#         return fac_memo[a]

#     ath_fac = a * factorial(a-1, fac_memo) # a! = a * (a-1)!
#     fac_memo[a] = ath_fac
#     return ath_fac

# n,k = map(int, input().split())
# print(factorial(n, memo) // (factorial(k, memo) * factorial(n-k, memo)))
