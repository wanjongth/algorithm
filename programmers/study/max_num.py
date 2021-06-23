# 가장 큰 수 - 정렬 - 42746

# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 순열 - all 시간 초과

# from itertools import permutations


# def solution(numbers):
#     answer = ''
#     per_arr = list(permutations(numbers, len(numbers)))

#     for i in per_arr[0]:
#         answer += str(i)

#     for i in range(len(per_arr)):
#         temp = ''
#         for j in per_arr[i]:
#             temp += str(j)
#             if int(answer) < int(temp):
#                 answer = temp

#     return answer

def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))

    for j in range(9, -1, -1):
        for i in numbers:
            for k in range(0, len(i)):
                # print('자릿수')
                # print(int(i[k]))
                # print('숫자')
                # print(j)
                if int(i[k]) == j:
                    answer += i
                    break
    # print(answer)
    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
