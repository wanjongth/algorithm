# 이중 우선순위큐 - 큐 - 42628
'''
중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

명령어	    수신 탑(높이)
I 숫자	   큐에 주어진 숫자를 삽입합니다.
D 1	      큐에서 최댓값을 삭제합니다.
D -1	  큐에서 최솟값을 삭제합니다.
이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때,
모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

제한사항
operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
operations의 원소는 큐가 수행할 연산을 나타냅니다.
원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.
'''

# 따로 해버리면, 삽입 삭제가 이미 이루어진 이후에 들어오는 것들은 반영이 안되어 틀린코드 -> 힙을 계속 변경하는 코드가 필요

# import heapq


# def solution(operations):

#     min_heap = []

#     other_operations = []
#     for operation in operations:
#         if operation[0] == 'I':  # 넣을때부터 음수를 표시 ? 그럴 필욘 없지
#             heapq.heappush(min_heap, int(operation.split()[-1]))
#         elif operation[0] == 'D' and operation.split()[-1] == '-1':
#             heapq.heappop(min_heap)  # 최소힙만 먼저 꺼냄
#         else:  # 나머지는 새로운 배열에 담음
#             other_operations.append(operation)

#     min_heap = list(map(int, min_heap))
#     if len(min_heap) == 0:
#         return [max(min_heap), min(min_heap)]

#     max_heap = []
#     for i in min_heap:
#         heapq.heappush(max_heap, -i)

#     print(other_operations)
#     for _ in range(len(other_operations)):
#         heapq.heappop(max_heap)

#     if len(max_heap) == 0:
#         return [0, 0]

#     return [-min(max_heap), -max(max_heap)]

# # nlargest라는게 있다. -> nlargest(n, heap) : n개의 가장 큰값들로 이루어진 리스트 반환
import heapq


# def solution(operations):
#     heap = []

#     for operation in operations:
#         a, b = operation.split()
#         if a == 'I':
#             heapq.heappush(heap, int(b))
#         else:
#             if len(heap) > 0:
#                 if b == '1':  # 최대 뺄 때
#                     heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
#                 else:  # 최소 뺄 때
#                     heapq.heappop(heap)

#     if len(heap) == 0:
#         return [0, 0]
#     else:
#         return [heapq.nlargest(1, heap)[0], heap[0]]


# 최대 최소에따라 반대 힙 반영
def changeHeap(old_heap):
    new_heap = []
    for num in old_heap:
        heapq.heappush(new_heap, -num)
    return new_heap


def solution(operations):
    answer = []  # [최댓값, 최솟값]
    min_heap = []
    max_heap = []

    for operation in operations:
        command, num = operation.split(' ')
        num = int(num)
        if command == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif command == 'D':
            # try: # 예외처리 안하면 프로그래머스에서 인덱스에러
            if num == 1:  # 최댓값 삭제
                heapq.heappop(max_heap)
                min_heap = changeHeap(max_heap)
            else:  # 최솟값 삭제
                heapq.heappop(min_heap)
                max_heap = changeHeap(min_heap)
            # except:
            #     continue

    if len(max_heap) != 0:
        answer.append(-max_heap[0])
    else:
        answer.append(0)
    if len(min_heap) != 0:
        answer.append(min_heap[0])
    else:
        answer.append(0)
    return answer


# print(solution(["I 16", "D 1"]))
# print(solution(["I 7", "I 5", "I -5", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642",
      "I 45", "I 97", "D 1", "D -1", "I 333"]))
