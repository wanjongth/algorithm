# import time
# time
# 처음 = time.time()
# while 처음 + 5 >= time.time():
#     pass
# print('5초있다가 출력')

# 가장 큰 수 만들기 - Remind

max_value = 0
a = 0
b = 0
for i in range(1, 99 + 1):
    j = 100 - i
    print(i, j)
    # 최댓값 구하기
    if max_value < i * j:
        max_value = i * j
        a = i
        b = j

print(a, b, max_value)

'''
# python continue 쓰는 이유 ?
# 다른 언어에서는 continue 키워드를 잘 쓰지 않는다고 한다. -> 들여쓰기 줄이기 위해 사용한다고 함
'''

# 반복문 거꾸로 돌리기
# 이제까지는 쓸 일이 있으면 range(시작,끝-1,-1)로 돌렸었는데
arr = [273, 52, 103, 32, 57]

# for i in reversed(range(끝값,시작값-1))로 돌릴 수 있다.
for i in reversed(range(0, 10)):
    print(i)

# 딕셔너리

# # 플랫팅? ->딕셔너리 요소 평평~ 하게 만들기
character = {
    'name': '기사',
    'level': 12,
    'items': {
        'sword': '검',
        'armor': '초보자용'
    },
    'skill': ['베기', '세게 베기', '아주 세게 베기']
}

for key in character:
    if type(character[key]) is dict:
        for k in character[key]:
            print('{} : {}'.format(k, character[key][k]))
    elif type(character[key]) is list:
        for item in character[key]:
            print('{} : {}'.format(key, item))
    else:
        print('{} : {}'.format(key, character[key]))

# # counter 구현
# numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
# counter = {}

# for number in numbers:
#     if number in counter:
#         counter[number] += 1
#     else:
#         counter[number] = 1

# print(counter)

'''
# 일회용 함수 : 제너레이터 - 사용할 곳에 직접 꼽아서 사용한다.
# reversed_a = reversed() 처럼 변수에 넣고 사용하게 되면 처음 한번만(일회용) 수행되게 된다.
* 리스트 뒤집기 : reversed() -> list(reversed(리스트)), for i in reversed(리스트)
* 현재 인덱스가 몇 번째인지 확인하기 : enumerate() - for i,v in enumerate() -> i,v는 (i,v)로 튜플 형태였다고 한다.
* 딕셔너리로 쉽게 반복문 작성하기: items()
-> for key in dictionary: 형태로 반복문을 돌릴 때, enumerate처럼 key,value를 사용하고 싶을 때
for key,value in dictionary.items(): 형태로 사용하게 된다.
'''

# 리스트 컴프리헨션(리스트 내포) - Remind
array = []
for i in range(0, 20, 2):
    array.append(i * i)
print(array)
array = [i*i for i in range(0, 20, 2)]
print(array)
array_2 = [i for i in range(10) if i % 3 == 0]
print(array_2)
'''
간단한 for문 돌릴 때, 2차원 배열 초기화 시 지속적으로 사용할 수 있도록 연습하자.
'''

# 진수 변환
bin_10 = '{:b}'.format(10)  # 2진수로 변환 -> '1010'
print(bin_10)
print(int(bin_10, 2))  # 10진수로 변환 -> 10

# 1 ~ 100 / 2진수 / 0이 하나만 포함된 숫자의 합
output = 0
for i in range(1, 101):
    if '{:b}'.format(i).count('0') == 1:
        print('{} : {:b}'.format(i, i))
        output += i
print(output)

# 리스트 내포
output = [i for i in range(1, 100 + 1) if '{:b}'.format(i).count('0') == 1]
print(sum(output))
