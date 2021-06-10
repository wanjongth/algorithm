# # # 지수 구하기
# def binary_test(n):
#     cnt = 0
#     while n >= 2:
#         cnt += 1
#         n = n/2
#     return cnt


def solution(n, a, b):
    cnt = 0

    while n > 2:
        # 홀수로 만들기
        if a % 2 == 0:
            a -= 1
        if b % 2 == 0:
            b -= 1
        # 비교할 중앙값
        mid = int(n/2)
        # 부호가 다르면
        if (mid-a) * (mid-b) < 0:
            cnt += 1
        elif (mid-a) * (mid-b) > 0 and abs(b-a) == int(mid/2):
            cnt += 1
        a = int((a+1)/2)
        b = int((b+1)/2)
        n = int(n/2)

    return cnt+1


# print(solution(8, 4, 7))
# # print(solution(8, 4, 5))
# print(solution(8, 1, 2))
# # print(solution(8, 2, 1))
# print(solution(8, 2, 3))
# print(solution(4, 2, 3))
# print(solution(4, 1, 3))
# print(solution(4, 1, 2))
for i in range(1, 8):
    print(solution(8, i, i+1))
