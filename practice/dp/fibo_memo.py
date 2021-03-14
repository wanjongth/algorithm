# #항해 99 스파르타 알고리즘 강의 자료
input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

# # print(memo[1])
# # 만약 메모에 있으면 그 값을 반환
# # 없으면 수식대로 구함
# # 그리고 그 값을 메모에 기록
# # 메모이제이션 - dict()형


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(
        n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo


print(fibo_dynamic_programming(input, memo))


# 기본 원칙 2가지
# 부분 문제 : 반복되는 형태로 문제가 계속해서 파생
# 메모이제이션 : 메모 만들어야겠다 생각
