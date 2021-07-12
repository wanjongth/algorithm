# 숫자 문자열과 영단어

'''
네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.
'''

# 첫번째 풀이, 중복인 경우나 낮은 내림차순이 될 경우 오류


def solution(s):
    answer = ''
    num_dict = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '0': 'zero'
    }

    for key in num_dict:
        if num_dict[key] in s:
            answer += key
        elif key in s:
            answer += key

    return int(answer)


def solution(s):
    num_dict = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '0': 'zero'
    }

    for key in num_dict:
        if num_dict[key] in s:
            s = s.replace(num_dict[key], key)

    return int(s)


print(solution("one4seveneight"))
print(solution('1zerotwozero3'))
print(solution('four1two5one'))
