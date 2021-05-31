# 성적이 낮은 순서로 학생 출력하기
# 학생의 이름과 학생의 성적으로 데이터가 주어질 때 성적이 낮은 순서대로(오름차순) 이름을 출력하는 프로그램

# 입력 조건
# 첫째 줄 N 두번째 줄부터 학생의 이름을 나타내는 문자열 A와 성적을 나타내는 정수 B가 공백으로 구분되어 입력
# 출력 -> 학생의 이름을 성적이 낮은 순서대로 출력

# 입력 예
# 2
# 홍길동 95
# 이순신 77

n = int(input())

array = []
for i in range(n):
    A, B = input().split()
    array.append((A, B))  # append 메서드는 하나의 argument만 가지므로 튜플로 넣어줌

# 람다식 이해 필요.. -> 키를 기준으로 정렬할 것이고 그 키는 student인데 그것은 튜플의 두번쨰 값이다.
array = sorted(array, key=lambda student: student[1])


# def student(array):
#     array = sorted(array, key=array[1])
#     return array


for student in array:
    print(student[0], end=' ')

# # 나올 때마다 찾아보게 되는 람다
# # lambda 인자 : 표현식


# def hap(x, y):
#     return x + y


# hap(10, 20)
# # 위를
# (lambda x, y: x + y)(10, 20)
