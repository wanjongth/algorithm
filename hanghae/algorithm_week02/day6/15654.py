# N과 M(5) - 백트래킹
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구해라
# N개의 자연수 중에서 M개를 고른 수열
# 사전순, 증가하는 순서대로 출력

n, m = map(int, input().split())


num = list(map(int, input().split()))
num.sort()
check = [False for i in range(n)]
# print(check)

array = []


def n_and_m(k):
    if k == m:
        print(*array)
        return
    # for i, v in enumerate(num):
    #     if check[i] == False:
    #         check[i] = True
    #         array.append(v)
    #         n_and_m(k+1)
    #         check[i] = False
    #         array.pop()
    for i in range(n):
        if check[i] == False:
            check[i] = True
            array.append(num[i])
            n_and_m(k+1)
            check[i] = False
            array.pop()


n_and_m(0)
