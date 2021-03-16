# 괄호 - 스택

# 괄호 문자열은 두 개의 괄호 기호인 '('와 ')'로만 구성되어 있는 문자열
# 괄호의 모양이 바르게 구성된 문자열은 올바른 괄호 문자열(Valid PS)
# 만약 x가 VPS라면 이것을 하나의 괄호에 넣은 새로운 문자열 (x)도 VPS

# 입력 : T개의 테스트데이터, 각 테스트 데이터의 첫째 줄에는 괄호문자열
# 출력 : VPS이면 YES 아니면 NO

# # 방법1
# # 리스트로 구현하려 했으나
# # pop 은 빈리스트일 경우 수행할 수 없기 때문에 복잡해졌음.. - 4949번 참고 후 방법2 구현
# # 아래 코드는 숫자로도 사용할 수 있다 정도로만 알아두고 방법 2를 익히고 활용하는게 좋을 것 같다
# # 숫자로 할 때 스택에 쌓는 조건이 여러 조건이면 순서가 뒤죽박죽 될 때의 조건을 구현하기 힘들다
# # ex) 4949.py

# import sys
# t = int(input())

# for i in range(t):
#     string = sys.stdin.readline()
#     sum = 0
#     for bracket in string:  # 문자열 안에 괄호들 검색
#         if bracket == '(':  # (가 나오면 쌓고
#             sum += 1
#         elif bracket == ')':  # )가 나오면 pop
#             sum -= 1
#         if sum == -1:  # pop 이 불가능 하지만 수로 구현하면 가능
#             print('NO')
#             break
#     if sum == 0:  # 만약에 남아있는 애들이 없으면
#         print('YES')  # (만큼 )가 왔다는 말이므로 yes
#     elif sum > 0:  # 남아있다면
#         print('NO')

# #4949번 참고하고 푼 코드..
# #상태 사용
import sys
t = int(input())

for i in range(t):
    string = sys.stdin.readline()
    stack = []
    answer = True  # 초기 상태 등록

    for bracket in string:
        if bracket == '(':  # '('가 나오면 스택에 쌓고
            stack.append(bracket)

        elif bracket == ')':  # ')'가 나왔는데
            if len(stack) == 0:  # 스택이 비어있으면
                answer = False  # 상태를 False로 바꾸고
                break  # 종료
            if stack[-1] == '(':  # 만약 스택의 제일 위에 '('가 있으면
                stack.pop()  # 뽑아냄
            else:  # 다른경우 False
                answer = False
                break
    if answer == True and len(stack) == 0:  # 만약 answer가 True이고 스택이 비어있으면
        # if answer == True and not stack:
        print("YES")
    else:  # 위의 조건을 충족하지 않는다면 NO 출력
        print("NO")


# # 방법3
# # 찾아본 리스트로 구현한 것 중 내 기준 제일 직관적인 코드
# # 함수에 넣어 출력 하지 않게 고쳐도.. 이상하게 나옴..
# # - 실력탓..
# import sys


# def bracket(string):
#     stack = []
#     for bracket in string:
#         if len(stack) == 0 and bracket == ')':
#             return 'NO'

#         if bracket == '(':
#             stack.append(bracket)
#         else:
#             if stack[-1] == '(':
#                 stack.pop()
#             else:
#                 return 'NO'
#     if len(stack) == 0:
#         return 'YES'
#     return 'NO'


# n = int(input().strip())
# for i in range(n):
#     string = sys.stdin.readline().strip()
#     print(bracket(string))
