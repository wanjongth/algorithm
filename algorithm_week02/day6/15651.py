# N과 M(3) - 백트랴킹
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구해라
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다. - 체크할 필요가 없다

n, m = map(int, input().split())

# check = [False for i in range(n)]
# print(check)
array = []


def n_and_m(k):
    if k == m:  # 종료조건
        print(*array)  # 원소 출력
        return
    for i in range(n):  # n만큼 반복
        array.append(i+1)  # 그 수 배열에 담고
        n_and_m(k+1)  # k값 증가하여 재귀
        array.pop()  # 배열 초기화


n_and_m(0)
