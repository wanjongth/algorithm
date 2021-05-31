# 내장함수 - 별도의 import 명령어 없이 바로 사용할 수 있는 함수 - input(), print() ...

# sum() - 리스트와 같은 iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환
result = sum([1, 2, 3, 4, 5])
print(result)

# min() - 파라미터가 2개 이상 들어왔을 때 가장 작은 값 반환
result = min([6, 2, 3, 4, 5])
print(result)

# max() - 파라미터가 2개 이상 들어왔을 때 가장 큰 값 반환
result = max([6, 2, 3, 4, 5])
print(result)

# eval() - 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과 반환
result = eval("(3 + 5) * 7")
print(result)

# sorted() - iterable 객체가 들어왔을 때 정렬된 결과 반환 / key 속성으로 정렬 기준 명시, reverse 속성으로 뒤집을지 여부 설정
result = sorted([9, 1, 8, 5, 4])
print(result)

result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

# 원소를 튜플의 두 번째 원소(수)를 기준으로 내림차순 정렬
result = sorted([('홍길동', 35), ('이순신', 50), ('아무개', 20)], key = lambda x: x[1], reverse=True)
print(result)

# iterable 객체는 기본으로 sort() 함수를 내장하고 있어 굳이 sorted() 함수 사용하지 않아도 됨
data = [9, 1, 8, 5, 4]
data.sort(reverse=True)
print(data)