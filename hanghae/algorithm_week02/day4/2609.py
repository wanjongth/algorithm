# 최대공약수와 최대공배수 - 정수 및 조합론
# 두 자연수를 입력받아 최대공약수와 최대공배수 출력

# 입력 - 두 개의 자연수
# 출력 - 첫째줄 : 두 수의 최대공약수 둘째줄 : 최소공배수
# #방법1 math 내장 라이브러리를 이용함
# import math

# a, b = map(int, input().split())

# gcd = math.gcd(a, b)
# print(gcd)
# lcm = gcd * a/gcd * b/gcd
# print(int(lcm))

# # 방법2
# def gcd2(a, b):
#     cd_list = []
#     if b > a:  # 두 수중에 작은 값 기준 잡기
#         (a, b) = (b, a)
#     for i in range(1, b+1):  # 두 수 중에 작은 값 까지만 나눠보면 됨
#         if a % i == 0 and b % i == 0:  # 둘이 동시에 나눠지는 i
#             cd_list.append(i)
#         # print(cd_list)
#         gcd2 = cd_list[-1]  # 제일 마지막 인덱스 값 = 최대공약수
#     return int(gcd2)


# a, b = map(int, input().split())
# gcd2 = gcd2(a, b)
# print(gcd2)
# lcm = gcd2 * a/gcd2 * b/gcd2
# print(int(lcm))


# # 방법3: 유클리드 호제법
# # 두 정수 a,b에 대해서 a>b일 때, a=bq+r 이라 하면
# # gcd(a,b)=gcd(b,r)이다.(단 0=<r)
# # 큰 숫자를 작은 숫자로 나누어 나머지를 구한다.
# # 나머지와 작은 숫자를 비교해서 마찬가지로 나누어 나머지를 구한다.
# # 나머지가 0이 될 때까지, 작은숫자가 최대공약수

# def gcd3(a, b):
#     if b > a:
#         (a, b) = (b, a)
#     while b > 0:
#         c = b  # 현재 작은값 c에 저장
#         b = a % b  # 나눈 나머지를 작은값으로 저장
#         a = c  # 기존의 작은값이 큰 값이 됨
#     return a


# a, b = map(int, input().split())
# gcd3 = gcd3(a, b)
# print(gcd3)
# lcm = gcd3 * a/gcd3 * b/gcd3
# print(int(lcm))
