# 힙 - 다익스트라 최단 경로 알고리즘 포함 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용
# 파이썬의 힙은 최소 힙으로 구성되어 있어 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 O(NlogN)에 오름차순 정렬 완료

import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽인된 모든 원소 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 최대 힙 구현할 때는 원소의 부호를 임시로 변경하는 방식 사용 - 힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸었다가, 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꿈

def heapsort2(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽인된 모든 원소 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)