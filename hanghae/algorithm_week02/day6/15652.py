# N과 M(4) - 백트래킹
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구해라
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다. -> 방문처리 안해도 됨
# 고른 수열은 비내림차순 - 길이가 K인 수열 A가
# A1=<A2=<...=<Ak-1=<Ak

n, m = map(int, input().split())


# print(check)
array = []


def n_and_m(k, start):
    if k == m:
        print(*array)
        return
    for i in range(start, n+1):  # 재귀돌때 i를 start에 넣어 증가시킴.
        array.append(i)
        n_and_m(k+1, i)
        array.pop()


n_and_m(0, 1)
