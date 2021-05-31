# 리스트 관련 메서드
a = [1, 4, 3]
print("기본 리스트:", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입: .append(값)", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬: .sort()", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: .sort(reverse=True)", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: .reverse()", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3추가: .insert(인덱스, 데이터)", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: .count(값)", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제 .remove(값)", a)

# insert() 함수를 사용할 때 원소의 개수가 N이면, 시간 복잡도는 O(N). insert() 함수를 남발하면 시간 초과 빈번
# remove() 의 시간 복잡도도 O(N)
# 다른 프로그래밍 언어에서는 remove_all()과 같은 함수로 간단하게 특정한 값을 가지는 모든 원소를 제거할 수 있음
# 하지만 파이썬의 경우 기본적으로 제공 X

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
# a에 포함된 원소를 하나씩 확인하며 그 원소가 remove_set에 포함되지 않을때만 result에 넣음
result = [i for i in a if i not in remove_set]
print(result)

# del 객체
a = [1, 2, 3, 4, 5]
del a[2:]
print(a)
