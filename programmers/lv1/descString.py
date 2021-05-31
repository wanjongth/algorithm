# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

def solution(s):

    answer = "".join(sorted(list(s), reverse=True))

    return answer

# 처음에는 ascii 값을 비교해서 해야하나 했다.(string 라이브러리의 ascii - lower, upper)
# 리스트 안 문자열 sorted는 자동으로 대소문자 비교를 해준다.

# 풀어쓰기


def solution(s):
    s = list(s)
    s.sort(reverse=True)
    answer = ""
    for i in s:
        answer = answer + i
    return answer
