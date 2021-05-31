# import sys

# # memo 라는 빈 딕셔너리 생성
# memo = {
# }

# # 만약 메모에 있으면 그 값 반환
# # 없으면 수식대로 구함
# # 그리고 그 값을 메모에 기록


# def w(a, b, c, memo):
#     if (a, b, c) in memo:
#         return memo[(a, b, c)]

#     if a <= 0 or b <= 0 or c <= 0:
#         memo[(a, b, c)] = 1
#         return 1
#     elif a > 20 or b > 20 or c > 20:
#         memo[(a, b, c)] = w(20, 20, 20, memo)
#         return w(20, 20, 20, memo)
#     elif a < b < c:
#         memo[(a, b, c)] = w(a, b, c-1, memo) + \
#             w(a, b-1, c-1, memo) - w(a, b-1, c, memo)
#         return w(a, b, c-1, memo) + w(a, b-1, c-1, memo) - w(a, b-1, c, memo)
#     else:
#         memo[(a, b, c)] = w(a-1, b, c, memo) + w(a-1, b-1, c, memo) + \
#             w(a-1, b, c-1, memo) - w(a-1, b-1, c-1, memo)
#         return w(a-1, b, c, memo) + w(a-1, b-1, c, memo) + w(a-1, b, c-1, memo) - w(a-1, b-1, c-1, memo)


# while True:
#     a, b, c = map(int, sys.stdin.readline().split())
#     if a == -1 and b == -1 and c == -1:
#         # if a and b and c == -1 and -1 and -1:
#         break
#     print('w({0}, {1}, {2}) = {3}'.format(a, b, c, w(a, b, c, memo)))


# # 풀이 2
import sys
input = sys.stdin.readline


def w(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
            w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c]


dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))

# # 풀이 3
# import sys
# input = sys.stdin.readline


# def w(a, b, c):  # w함수 정의
#     global memo  # 전역변수로 memo 선언. 함수 안과 밖에서 사용하기 위함

#     if (a, b, c) in memo.keys():  # 만약 튜플 (a,b,c)가 memo의 키 값에 있다면
#         return memo[(a, b, c)]  # memo 의 그 값 반환

#     if a <= 0 or b <= 0 or c <= 0:  # 만약 a 또는 b 또는 c 가 0보다 작거나 같다면
#         return 1  # 1 반환

#     elif a > 20 or b > 20 or c > 20:  # 만약 a 또는 b 또는 c가 20보다 크다면
#         memo[(20, 20, 20)] = w(20, 20, 20)  # memo에 w(20,20,20) 값 기록
#         return memo[(20, 20, 20)]  # memo 값 반환

#     elif a < b < c:  # 만약 a<b<c 라면
#         memo[(a, b, c)] = w(a, b, c-1) - w(a, b-1, c-1) + \
#             w(a, b-1, c)  # memo에 w함수 값 기록
#         return memo[(a, b, c)]  # memo 값 반환

#     else:
#         memo[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + \
#             w(a-1, b, c-1) - w(a-1, b-1, c-1)  # \은 줄바꿈 기능
#         return memo[(a, b, c)]


# while True:
#     x, y, z = map(int, input().split())

#     if x == -1 and y == -1 and z == -1:  # 입력의 마지막 조건 (탈출조건)
#         break

#     memo = {}
#     # .format(): 입력한 값의 형식 지정. 괄호{}로 표시된 위치에 지정된 형식의 문자열을 대체함
#     print('w({}, {}, {}) = {}'.format(x, y, z, w(x, y, z)))
