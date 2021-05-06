# 같은 숫자는 싫어
# arr 의 원소는 0~9까지로 이루어져 있다.
# 연속적으로 나타나는 숫자는 하나만 남기고 제거,
# 원소들의 순서를 유지해야 한다.


def solution(arr):
    answer = []
    for num1, num2 in zip(arr, arr[1:]):
        if num1 != num2:
            answer.append(num1)
    answer.append(arr[-1])
    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
