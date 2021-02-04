import math


# 소수 판별 함수
def prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인
    for i in range(2, x):
        # x로 나누어 떨어지면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수

print(prime_number(4))
print(prime_number(7))

# 위는 O(X)의 시간 복잡도를 가진다.
# 제곱근 까지만 나누어 떨어지는지 확인한다면 시간 복잡도를 줄일 수 있다 O(X^1/2)


def add_sqrt_prime_number(x):
    # 2부터 x의 제곱근까지 모든 수 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print(add_sqrt_prime_number(4))
print(add_sqrt_prime_number(7))

# 범위 소수 판별 - 에라토스테네스의 체

n = 1000
array = [True for i in range(n+1)] # 모든 수가 True인 것으로 초기화(0,1 제외)

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수 확인
    if array[i] == True: #i가 남은 수인 경우
        # i를 제외한 i의 모든 배수 지움
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 소수 출력
for i in range (2, n+1):
    if array[i]:
        print(i, end=' ')



