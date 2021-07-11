# from os import close


# file = open('text.txt', 'a')
# file.write('ㅎㅇ')
# file.close()


# file = open('text.txt', 'r')
# print(file.read())
# file.close()
'''
파일을 읽고 쓰는 코드
어떤 대상
- 텍스트 파일: 텍스트에디터로 열 수 있는 것
- 바이너리 파일 : 텍스트에디터로 열 수 없는 것(이미지,동영상,워드,엑셀,pdf 등)

어떻게 다룰 것인가
- 쓰기
  - 새로(write) : w
  - 있는 파일 뒤에(append) : a
- 읽기(read) : r
'''

# # with 구문 -> open, close
# with open('text.txt', 'a') as file:
#     file.write('ㅎㅇ')
# with open('text.txt', 'r') as file:
#     print(file.read())


# 제너레이터
def 함수():
    print('출력 1')
    yield 100  # 코드의 진행 양보
    print('출력 2')
    yield 200


제너레이터 = 함수()
print('제너레이터 : ', 제너레이터)
# next(제너레이터)
# next(제너레이터)
# next(제너레이터)  # 오류 - StopIteration

for i in 제너레이터:
    print(i)


# 메모리를 두배로 쓰지 않는다
def 반전(리스트):
    for i in range(len(리스트)):
        yield 리스트[-i - 1]


제너레이터 = 반전([1, 2, 3, 4, 5])
for i in 제너레이터:
    print(i)

# 맵의 활용
numbers = [1, 2, 3, 4, 5, 6]
print('::'.join(map(str, numbers)))  # 안바꾸면 원소가 정수라서 에러


# 람다 연습
numbers = list(range(1, 10 + 1))
print('# 홀수만 추출')
print(list(filter(lambda x: x % 2 == 1, numbers)))

print('# 3이상 7 미만')
print(list(filter(lambda x: x >= 3 and x < 7, numbers)))

print('# 제곱해서 50미만 추출')
print(list(filter(lambda x: x**2 < 50, numbers)))
