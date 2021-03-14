# 설탕공장 - 기본수학
# 사탕 가게에 설탕을 N킬로그램 배달
# 설탕 공장에서 만드는 설탕은 3킬로그램 봉지, 5킬로그램 봉지
# 최대한 적은 봉지를 들고 가려 함

# 입력 : N
# 출력 : 배달하는 봉지의 최소 개수, 반례 : -1로 출력


# # 신박한 풀이
# n = int(input())


# def sugar(N):
#     for i in range((N//3)+1):  # 3킬로그램 봉지 개수(i = 0, ... , N//3)
#         for j in range((N//5)+1):  # 5킬로그램 봉지 개수(j = 0, ... , N//5)
#             if ((5*j + 3*i) == N):  # i와 j 가 0부터 시작하기 때문에
#                 return j+i
#     return -1


# print(sugar(n))

# 대표적인 풀이
n = int(input())  # 설탕 무게

bag = 0  # 봉지 개수

while n >= 0:  # 왜 0만 됨? 3이면 -> 6을 넣었을 때 0이 되었을 경우 출력을 하지 못함
    if n % 5 == 0:  # 5의 배수이면
        bag += (n//5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    n -= 3
    bag += 1  # 5의 배수가 될 때까지 설탕 -3, 봉지 +1
else:
    print(-1)

# # 망한 풀이
# # 큰 케이스를 나누고 세부 케이스 생각
# # case1: n을 5로 나눴을때 나머지가 없다면 n//5
# #                      나머지가 3의 배수라면 n//5 + n//3
# #                                   아닐 경우

# # case2:
# #       n이 3의 배수인지 확인
# #           n 이 3의 배수라면 n//3
# #           n 이 3의 배수가 아니라면 return -1
# #           n-5 가 3의 배수일 경우
# #               n-5 // 3 +1

# # case3:
# #       n이 3의 배수도 5의 배수도 아니지만 3의 배수와 5의 배수로 조합해서 만들 수 있는 수
# #       .... 무한히 반복함..


# n = int(input())


# def sugar(n):
#     if n % 5 == 0:  # 5의 배수이면
#         return print(n//5)
#     elif n % 5 != 0:  # 5의 배수가 아니면
#         if n % 5 % 3 == 0:  # n을 5로 나눈 나머지가 3의 배수이면
#             return print((n // 5) + (n % 5 // 3))
#         elif n % 3 == 0:  # n이 3의 배수라면
#             return print(n//3)
#         # n이 3의 배수도, 5의 배수도 아니라면 (ex 8, 11, 14, 17 ,,)
#         # 3의 배수와 5의 배수를 조합해서 만들수 있는 수
#         elif n % 8 == 0:
#             return print(n // 8 * 2)
#         elif n % 8 % 5 == 0:
#             return print((n // 8 * 2) + (n % 8) // 5)
#         elif n % 8 % 3 == 0:
#             return print((n // 8 * 2) + (n % 8) // 3)
#         else:
#             return print(-1)


# sugar(n)