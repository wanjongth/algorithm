# 내적
# a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)


def solution(a, b):
    answer = 0

    for i, j in zip(a, b):
        answer += i*j
    return answer


a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]

print(solution(a, b))
