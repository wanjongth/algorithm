# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때,
# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수,
# solution을 완성해주세요.

# 1
def solution(phone_number):
    answer = ''

    temp = len(phone_number[0:-4])
    answer = phone_number.replace(phone_number[0:-4], '*'*temp)

    return answer

# 슬라이싱만 이용해서 풀 수 있음


def solution(s):
    return "*"*(len(s)-4) + s[-4:]


print(solution("12345555556"))
