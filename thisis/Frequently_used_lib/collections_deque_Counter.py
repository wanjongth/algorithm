# 보통 파이썬에서는 deque을 사용해 큐를 구현
# 리스트 자료형은 append() 메서드로 데이터를 추가하거나 pop() 메서드로 데이터를 삭제할 때 가장 뒤쪽 원소를 기준으로 수행
# 띠라서 앞쪽에 있는 원소를 처리할 때에는 덱을 사용하는게 유리

# deque은 인덱싱, 슬라이싱 등의 기능을 사용할 수 없으나, 연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입, 삭제할 때는 효과적으로 사용될 수 있다.
# deque은 스택이나 큐의 기능을 모두 포함한다고 볼 수 있기 때문에 스택 혹은 큐 자료구조의 대용으로 사용될 수 있다.

# 첫번째 원소를 제거할 popleft(x) 마지막 원소 제거 pop(x), 첫번째 원소 삽입 appendleft(x) 마지막 원소 삽입 append(x)
# 따라서 deque를 큐 자료구조로 이용할 때, 원소를 삽입할 때는 append()를 사용하고 삭제할 때는 popleft() 사용

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

# Counter는 등장 횟수를 세는 기능 제공 - 해당 객체 내부의 원소가 몇 번씩 등장했는지 알려줌

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))