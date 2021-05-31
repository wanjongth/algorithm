# 두 정수 사이의 합
# 두 정수 a,b가 주어졌을때 사이에 속한 모든 정수의 합 리턴

def solution(a, b):
    answer = 0

    if a == b:
        return a
    elif a < b:
        for i in range(a, b+1):
            answer += i
    else:
        for i in range(b, a+1):
            answer += i

    return answer


# 최대 최소 이용 -> 범위 합
def solution2(a, b):
    answer = 0
    answer = sum(range(min(a, b), max(a, b)+1))
    return answer


print(solution2(3, 5))
