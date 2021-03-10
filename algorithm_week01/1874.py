# N = int(input())
# array = []*N

# for num in range(N):
#     target = int(input())

#     if num < target:
#         for _ in array:
#             array.append(num)
#             print("+")
#     elif num == target:
#         array.pop()
#         print("-")

#     else:
#         print("NO")
#         break

N = int(input())
array = []*N
plus_minus = []
count = 1
validate = True

for _ in range(N):
    target = int(input())
    while count <= target:  # count와 들어온 숫자가 같아질때 까지
        array.append(count)  # count를 array에 추가
        plus_minus.append('+')  # 추가할때마다 plus_minus 리스트에 +추가
        count += 1
    if array[-1] == target:  # array의 마지막 인덱스가 target과 같아지면
        array.pop()  # 젤 위에꺼 제거하고
        plus_minus.append('-')  # plus_minus 리스트에 - 추가
    else:
        validate = False  # 위의 조건을 만족하지 못하면 상태를 False로 바꿔줌
        break

if validate == False:
    print('NO')
else:
    for i in plus_minus:
        print(i)
