# 기본수학 - Fly me the Alpha Centauri
# 공간이동 장치
# 이동 거리
# 이전 작동시기에 k 광년을 이동한다면 다음 작동에는 k-1, k , k+1 이동가능
# ex) 처음 : k = 0 , 다음 작동에는 -1, 0 , 1 중 음수와 0은 필요없으므로 1 이동가능
#     k = 1 이면 다음 작동에는 1, 2, 3 이동할 수 있음

# 도착 직전에, 이동거리는 반드시 1
# x부터 y 까지 이동하는 데, 이동 횟수의 최솟값 구해라

# 입력 : 테스트케이스 : T, 각각의 테스트 케이스에 대해 x,y

# import math
# num = int(input())

# # 패턴을 알기 위해 y - x 값으로 노가다 해보면,,
# #   f(1),2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12...
# # 예) 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, ...
# # 위와 같이 증가하는 수열을 찾으려고 했는데,, 잘 안나와서
# # 풀라고 만든 문제 맞나
# # 다시 검색과 노가다를 통해.. 결론 도출 - 루트 4n-1 or 루트 4n-2 or 루트 4n-3을 내림해주면 됩니다..

# for i in range(num):
#     x, y = map(int, input().split())
#     diff = y - x
#     print(int(math.sqrt(4*diff-1)))


# 다른 코드
case = int(input())
for i in range(case):
    x, y = map(int, input().split())
    distance = y - x
    count = 0  # 이동횟수
    move = 1  # 1만큼 이동하는건 작동하는순간 무조건 일어나는 일이기 때문.
    move_distance = 0
    while move_distance < distance:  # 최대 이동거리 < 이동하고자하는 거리 를 벗어나면 이동이 발생
        count += 1  # 이동 발생
        move_distance += move  # 이동발생 시, 최대이동거리도 늘어남
        if count % 2 == 0:
            move += 1  # 이동횟수가 짝수가 될 때 마다 move distance값이 1씩 오름
    print(count)
