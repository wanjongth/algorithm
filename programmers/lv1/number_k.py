# K번째수
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때 k번째 수(command)
# 배열에 담아 출력

def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        answer.append(
            sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])

    return answer


def solution2(array, commands):
    answer = []
    for i, j, k in commands:  # i, j, k 를 따로 입력 받는다..
        answer.append(sorted(array[i-1:j])[k-1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
print(solution2([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
