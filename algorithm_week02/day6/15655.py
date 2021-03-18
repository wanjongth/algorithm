# N과 M(6) - 백트래킹
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구해라
# N개의 자연수 중에서 M개를 고른 수열, 고른 수열은 오름차순이어야 함
# 사전순, 증가하는 순서대로 출력

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.append(0)  # 1부터 세야해서 입력 기준이 자연수이므로 0을 추가해줬음
num.sort()

# print(num)
array = []
check = [False for _ in range(n+1)]


def n_and_m(k, start):
    if k == m:
        print(*array)
        return
    for i in range(start, n+1):  # enumerate는 시작값을 조정해도 끝값을 조정할 수 없어서
        if check[i] == False:
            check[i] = True
            array.append(num[i])
            n_and_m(k+1, i)
            check[i] = False
            array.pop()


n_and_m(0, 1)
