# 집합 - 중복 불허 / 순서가 없음
# 리스트와 튜플은 순서가 있기 때문에 인덱싱 가능 - 반면 딕셔너리와 집합은 순서가 없기 때문에 인덱싱 불가

# set()이용 / {} 이용

# 집합 자료형 초기화 방법1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)
# 집합 자료형 초기화 방법2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 집합 연산

a = set([1,2,3,4,5])
b = set([3,4,5,6,7,])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

# 집합 관련 함수

data = {1,2,3}
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 여러개 추가
data.update([5,6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)