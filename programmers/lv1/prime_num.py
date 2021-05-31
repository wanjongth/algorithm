import math


def solution(n):
    array = [True for i in range(n+1)]  # 모든 수가 True인 것으로 초기화

# 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1):  # 2부터 n의 제곱근까지의 모든 수 확인
        if array[i] == True:  # i가 남은 수인 경우
            # i를 제외한 i의 모든 배수 지움
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    # 0,1 제외하고 출력
    return array.count(True)-2


# 응용 - 에라토스테네스의 체 차집합 이용하기
def solution(n):
    num = set(range(2, n+1))

    for i in range(2, int(math.sqrt(n)) + 1):
        if i in num:
            num -= set(range(2*i, n + 1, i))
            print(num)

    return len(num)


print(solution(10))
