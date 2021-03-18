# N과 M(2) - 백트레킹
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구해라
# 1부터 N까지 자연수 중 중복 없이 M개를 고른 수열 출력

n, m = map(int, input().split())

check = [False for i in range(n)]
print(check)
array = []


def n_and_m(k):
    if k == m:
        print(*array)  # 파이썬 언패킹 ! 괄호를 없애준다
        return

    for i in range(n):
        if check[i] == False:
            check[i] = True
            array.append(i+1)

            n_and_m(k+1)
            check[i] = False
            array.pop()


n_and_m(0)
