# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
import math


def solution(n):
    answer = 0

    if math.sqrt(n).is_integer():
        answer = int((math.sqrt(n)+1)**2)
    else:
        answer = -1

    return answer


print(solution(25))

# -> import math 안하고 풀면
# sqrt = n ** (1/2)이므로 이걸 이용하면 된다.
