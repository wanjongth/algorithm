# 문자열 뒤집기
# 0,1로만 이루어진 문자열 S
# 모든 숫자를 같게 만드려고 함
# S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집음
# 최소 횟수 출력

# 입력
# 0과 1로 이루어진 문자열 S,
# 출력
# 최소 횟수

def solution(string):
    cnt0 = 0  # 전부 0으로
    cnt1 = 0  # 전부 1로

    if string[0] == '1':
        cnt0 += 1
    else:
        cnt1 += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '1':  # 다음 수에서 1로 바뀌는 경우
                cnt0 += 1
            else:
                cnt1 += 1

    print(cnt0, cnt1)
    return min(cnt0, cnt1)


string = input()

print(solution(string))
