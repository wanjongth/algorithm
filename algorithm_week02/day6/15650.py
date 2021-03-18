# # N과 M(2) - 백트레킹
# # 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구해라
# # 1부터 N까지 자연수 중 중복 없이 M개를 고른 오름차순 수열

# # 방법 1: itertools - combinations . 이 문제는 백트레킹 관련 문제이므로 좋은 풀이는 아님
# from itertools import combinations
# n, m = map(int, input().split())

# array = []
# for i in range(1, n+1):
#     array.append(i)  # 1~n 까지 배열에 담음

# # print(array)

# result = (list(combinations(array, m)))  # 순서를 고려하지 않고 중복없이 m개를 고름.(튜플로반환)
# print(result)
# for i in result:
#     print(' '.join(map(str, i)))  # 튜플로 받아온 값을 괄호 없이 문자열로 출력


# #백트레킹
n, m = map(int, input().split())

check = [False for i in range(n+1)]  # 특정 수가 쓰였는지 체크
# start 때문에 인덱스 1부터 사용하기 위해 n+1 길이로 생성
# print(check)
array = []  # 수열을 담을 배열


def n_and_m(k, start):  # 전 문제와 다른점. 오름차순을 위해 start를 추가해줌
    if k == m:  # m개 모두 택했다면 배열 출력
        print(*array)  # 파이썬 언패킹 ! 괄호를 없애준다
        return

    for i in range(start, n+1):  # k!=m일 때 start부터 n까지의 수를 차례로 확인
        if check[i] == False:  # 안쓰였다면
            check[i] = True  # 쓴걸로 처리하고
            array.append(i)  # 배열에 담는다

            n_and_m(k+1, i+1)  # k를 증가시키고 재귀
            check[i] = False  # 초기화
            array.pop()  # 초기화


n_and_m(0, 1)
