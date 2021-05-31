n, m = map(int, input().split())

array = list()  # 결과 값을 담을 리스트 초기화
check = [False for _ in range(n)]  # 방문 내역


def n_and_m(k):
    if k == m:  # 종료조건 - k = m
        print(*array)  # 언패킹 기능 - 리스트의 원소를 괄호를 제거하고 나타냄
        return
    for i in range(n):
        if check[i] == False:  # 방문하지 않았다면
            check[i] = True  # 방문 체크
            array.append(i+1)  # 리스트에 넣어주고
            n_and_m(k+1)  # k값을 증가하여 재귀
            check[i] = False  # 방문 초기화
            array.pop()  # 리스트 초기화


n_and_m(0)
