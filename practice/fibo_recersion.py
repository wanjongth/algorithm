input = 40


def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765

# 재귀 단점 :n 이 좀 커지면 너무 오래걸림
# Fibo(3)
# Fibo(2) + Fibo(1) -> 1, 1 연산량 2

# Fibo(4)
# Fibo(3) + Fibo(2) -> 2, 1 연산량 3

# Fibo(5)
# Fibo(4) + Fibo(3) -> 3, 2 연산량 5
# 전에 했던걸 기억하기 위한 DP가 필요함
