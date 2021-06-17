# 이분탐색 - 순위 검색 - 72412
# 지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info,
# 개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,
# 각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

from itertools import combinations


# def solution(info, query):
#     answer = []
#     new_query = []
#     for i in query:
#         new_query.append(i.replace(" and", ""))
#     print(new_query)

#     # 점수 조건 먼저 구해놓고 새로운 배열에 Info 와 쿼리를 넣는다.
#     # 나머지는 쿼리와 비교해서 같으면 cnt + 1(or - 포함)
#     # 새로운 풀이 필요, split으로 뽑아낸 것들은 문자열이였기때문에 int로 변환해주어야 했다.

#     for i in range(len(query)):
#         cnt = 0
#         for j in range(len(info)):
#             # print('info는')
#             # print(info[j].split()[-1])
#             # print('query는')
#             # print(new_query[i].split()[-1])
#             if (int(info[j].split()[-1]) >= int(new_query[i].split()[-1])):
#                 cnt += 1
#             # print('cnt는')
#             # print(cnt)
#         answer.append(cnt)

#     return answer


# test case -> [1,1,1,1,2,4]
info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

# print(info[0].split())
# print(query[0].split(" and "))
# print(query[0].split("and")[-1].split()[0])
# print(solution(info, query))

# 특정 쿼리의 개발언어, 직군, 경력, 소울푸드 까지는 Key 값을 통해서 필터링을 해주고,
# 앞의 조건들이 일치했다면 점수들은 Value 에 있는 배열내에서 찾아 줌


def make_all_cases(temp):
    cases = []
    for i in range(5):
        for combination in combinations([0, 1, 2, 3], i):
            case = ''
            for idx in range(4):
                if idx not in combination:
                    case += temp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases


def get_lower_bound(target, array):
    current_min = 0
    current_max = len(array)

    while current_min < current_max:
        current_guess = (current_min + current_max) // 2
        if array[current_guess] >= target:
            current_max = current_guess
        else:
            current_min = current_guess + 1

    return current_max


def solution(info, query):
    answer = []
    all_cases_from_users = {}
    for user_info in info:
        user_info_array = user_info.split()
        all_cases_from_user = make_all_cases(user_info_array)
        for case in all_cases_from_user:
            if case not in all_cases_from_users.keys():
                all_cases_from_users[case] = [int(user_info_array[4])]
            else:
                all_cases_from_users[case].append(int(user_info_array[4]))

    for key in all_cases_from_users.keys():
        all_cases_from_users[key].sort()

    for query_info in query:
        query_info_array = query_info.split()
        case = query_info_array[0] + query_info_array[2] + \
            query_info_array[4] + query_info_array[6]
        if case in all_cases_from_users.keys():
            target_users = all_cases_from_users[case]
            answer.append(
                len(target_users) -
                get_lower_bound(int(query_info_array[7]), target_users)
            )
        else:
            answer.append(0)

    return answer


print(solution(info, query))
