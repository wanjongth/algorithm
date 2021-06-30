# 수식 최대화

# https://programmers.co.kr/learn/courses/30/lessons/67257

# def solution(expression):
#     temp = ''

#     num = ''
#     cal = []
#     for i in range(len(expression)):
#         if not expression[i].isdecimal():
#             num += ' '
#             cal.append(expression[i])
#             continue
#         if expression[i].isdecimal():
#             num += expression[i]
#     num = num.split()
#     print(num, cal)


#     return abs(eval(expression))


def calc(priority, n, expression):
    # priority 연산자 우선순위 모음 / n 우선순위 --> 낮은 것부터 0, 1, 2 / expression 더 낮은 우선순위에서 쪼개진 식 문자열
    if n == 2:  # 가장 높은 우선순위에 도달했을 때, 계산한다.
        return str(eval(expression))
    if priority[n] == '*':  # 먼저 쪼갠 애들부터 계산한다.
        res = eval('*'.join([calc(priority, n+1, e)
                   for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n+1, e)
                   for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n+1, e)
                   for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    # 이걸 쓰든, permutations 쓰든
    priorities = [
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*')
    ]
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer

# https://soniacomp.medium.com/%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%88%98%EC%8B%9D%EC%B5%9C%EB%8C%80%ED%99%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-e43e53ae19b6


# def solution(expression):
#     operations = [('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'),
#                   ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+')]
#     answer = []
#     for op in operations:
#         a = op[0]
#         b = op[1]
#         temp_list = []
#         for e in expression.split(a):
#             temp = [f"({i})" for i in e.split(b)]
#             temp_list.append(f'({b.join(temp)})')
#         answer.append(abs(eval(a.join(temp_list))))
#     return max(answer)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
