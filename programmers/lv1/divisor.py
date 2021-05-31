# 나누어 떨어지는 숫자 배열
# 백준에서 풀었던 기억이

def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    answer.sort()

    if len(answer) == 0:
        return [-1]

    return answer


print(solution([5, 8, 7, 10], 5))

# 프로그래머스 한 줄 코드;;


def solution(arr, divisor): return sorted(
    [n for n in arr if n % divisor == 0]) or [-1]
