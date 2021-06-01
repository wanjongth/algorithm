# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# 초기값 때문에 헷갈렸다. 2차원 행렬은 연습이 많이 필요하다.
def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr1[0])):
            arr.append(arr1[i][j] + arr2[i][j])
        answer.append(arr)

    return answer


# print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))
