# 입력을 최대한 빠르게 받은 경우 - 흔히 정렬, 이진 탐색, 최단 경로 문제  예를 들어 1,000만 개가 넘는 라인이 입력되는 경우
# 단순히 input() 함수를 그대로 사용하지는 않음

# sys 라이브러리에 정의되어 있는 sys.stdin.readline() 함수를 이용
# 한 줄 입력을 받고 나서 rstrip() 함수 호출
# readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데 이 공백 문자를 제거하려면 rstrip() 사용
import sys
# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)