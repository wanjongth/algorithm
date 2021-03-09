import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)

result = 0
while (start <= end):
    mid = (start + end) // 2
    total = 0  # 현재 잘린 나무들의 합
    for tree in trees:
        # 자르면
        if tree > mid:  # tree가 자르는 값보다 클때만 저장하므로
            total += tree - mid
    # 나무의 양이 부족한 경우
    if total < M:
        end = mid - 1  # 끝값을 중간값의 -1로 이동
    # 충분한 경우
    else:
        # 최대한 덜 잘랐을때가 정답이므로 여기서 result에 기록
        result = mid
        start = mid + 1  # 첫값을 중간값의 +1로 이동

print(result)
