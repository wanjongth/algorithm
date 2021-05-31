# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

def solution(s):
    if s[0] == '+':
        return int(s[1:])
    elif s[0] == '-':
        return -int(s[1:])
    else:
        return int(s)


print(solution('1234'))

# int 는 앞의 부호를 알아서 처리해준다. - 나중에 알게된 사실


def solution(str):
    a = int(str)
    return a
