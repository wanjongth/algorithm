# 문자열 압축 -> 프로그래머스
# 간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데,
#  이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다.
#  "어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

# 답안
def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer


s1 = 'aabbaccc'
s2 = 'ababcdcdababcdcd'
s3 = 'abcabcdede'
s4 = 'abcabcabcabcdededededede'
s5 = 'xababcdcdababcdcd'

print(solution(s1))
