# 기본수학 - 베르트랑 공준

# 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재

# 입력 : 여러 개의 테스트 케이스
# 입력의 마지막에는 0

# 출력 : 각 테스트 케이스에 대해 n보다 크고 2n보다 작거나 같은 소수의 개수 출력
# 제출은 pypy 로 합시다.

import math
import sys


def prime_number(x):  # 순환하여 소수판별하는 함수
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):  # 2부터 x의 제곱근까지
        if x % i == 0:  # 나누어 떨어지는 값이 있다면 소수가 아님
            return False
    return True


# print(prime_number(1))

while True:
    count = 0
    # 입력을 여러 줄 받으므로 sys.stdin.readline()을 사용하자!
    num = int(sys.stdin.readline())
    if num == 0:  # 입력의 마지막에 0이 들어오므로 0이 오면 반복 빠져나감
        break
    for i in range(num+1, 2*num+1):  # n보다 큰 숫자부터 이므로 num+1 부터 !
        if prime_number(i) == True:  # 들어온 숫자부터 2배까지 소수판별, 소수면 True 이므로
            count += 1  # count 해줌
    print(count)
