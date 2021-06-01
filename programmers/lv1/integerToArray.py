# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 잘못된 코드 -> 정렬로 접근하면 안됨 -> 뒤집기
def solutionX(n):
    answer = []

    for i in str(n):
        answer.append(int(i))
        answer.sort(reverse=True)
    return answer

# 반복문 거꾸로 돌기


def solution(n):
    answer = []
    n = str(n)

    for i in range(len(n)-1, 0-1, -1):
        answer.append(int(n[i]))
    return answer

# 사실 반복문 거꾸로 돌 필요도 없음 -> 다 계산하고 배열 reverse


def solution(n):
    answer = []
    n = str(n)

    for i in n:
        answer.append(int(i))

    answer.reverse()
    return answer


print(solution(12345))
