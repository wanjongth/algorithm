# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
# 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

def solution(s):
    answer = []
    array = s.split(" ")

    for i in range(len(array)):
        for j in range(len(array[i])):
            if j % 2 == 0:
                answer.append(array[i][j].upper())
            else:
                answer.append(array[i][j].lower())
        answer.append(" ")

    answer = ''.join(answer[:-1])

    return answer


print(solution("try hello  world"))

# 위에서 split()로는 연속된 공백이 나올때의 처리를 제대로 할 수 없음. -> split(" ")
# 또, 정답을 출력할 때 strip으로 공백을 제거했었는데 테스트 케이스 실패함 ???? 일단 슬라이싱으로 해결

# 아래에서 isalpha()로, 인덱스 처리를하면서 공백이 나올 경우에는 인덱스를 0으로 초기화시킨다.


def solution(s):
    answer = ""
    idx = 0
    for i in s:
        if i.isalpha():
            idx += 1
            if idx % 2 != 0:
                answer += i.upper()
            else:
                answer += i.lower()
        else:
            idx = 0
            answer += ' '
            continue

    return answer
