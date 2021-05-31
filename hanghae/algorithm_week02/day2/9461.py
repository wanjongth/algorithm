# 파도반 수열
# 삼각형의 변의 길이.
# 나선에서 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 K인 삼각형 추가

# 1, 1, 1, 2, 2, 3, 4, 5, 6, 9, 12, 16, 21, 28

# f(1)~f(3) = 1,
# f(4) = f(1) + f(2)
# f(5) = f(2) + f(3)
# f(6) = f(3) + f(4)
# ....
# f(n) = f(n-3) + f(n-2) --> 재귀: 시간초과

# # 메모이제이션
import sys
t = int(input())

# f(1)~ f(3) 저장 - f(4)를 만드는데 f(1), f(2) 필요하므로
memo = {
    1: 1,
    2: 1,
    3: 1
}


def padovan(n, memo):
    if n in memo:  # n이 메모에 있으면
        return memo[n]  # 해당하는 값 반환

    side_length = padovan(n-3, memo) + padovan(n-2, memo)  # 변의길이 변수에 넣어주고
    memo[n] = side_length  # 메모에 저장
    return side_length


for i in range(t):
    n = int(sys.stdin.readline())
    print(padovan(n, memo))


# #재귀 - 시간초과
# t = int(input())


# def padovan(n):
#     if n < 4:
#         return 1
#     elif n >= 4:
#         return padovan(n-3) + padovan(n-2)


# for i in range(t):
#     n = int(sys.stdin.readline())
#     print(padovan(n))
