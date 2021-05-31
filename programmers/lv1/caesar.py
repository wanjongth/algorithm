# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다.
# "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

def solution(s, n):
    answer = ''
    print(ord('a'))
    for i in s:
        # 공백
        if ord(i) == 32:
            answer += " "
        # 대문자 범위 초과
        elif 65 <= ord(i) <= 90 and ord(i)+n > 90:
            answer += chr(ord(i)-25+n-1)
        # 소문자 범위 초과
        elif 97 <= ord(i) <= 122 and ord(i)+n > 122:
            answer += chr(ord(i)-25+n-1)
        # 정상 범위
        else:
            answer += chr(ord(i)+n)
    return answer


print(solution(" AB", 1))
