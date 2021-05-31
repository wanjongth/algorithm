# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수
# solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

def solution(s):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i not in num:
                return False
        return True  # 여기서 True처리를 안해주면 len 비교를 못한다.

    return False

# isdigit이 있었다.


def solution(s):

    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
    return False

# 예외처리로 푸는법


def alpha_string46(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6
