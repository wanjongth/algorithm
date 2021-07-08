# 함수
# python의 가변 매개변수 -> print() 같이

def 함수이름(매개변수1, 매개변수2, *가변매개변수):
    print(매개변수1)
    print(매개변수2)
    print(가변매개변수)


함수이름(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
'''주의점
가변 매개변수는 마지막 위치에 와야한다.
한 함수에는 하나만 적용된다.
'''

# 기본 매개변수(default)


def print_n_times(value, n=5):
    for i in range(n):
        print(value)
# 기본 매개변수는 마지막에 입력한다.(앞에 쓰게 된다면 다른 변수들을 무조건 써야되므로 의미가 없어진다.)

# 가변, 기본 매개변수의 조합


def function(일반매개변수A, 일반매개변수B, *가변매개변수, 기본매개변수A=10, 기본매개변수B=20):
    print(일반매개변수A, 일반매개변수B)
    print(가변매개변수)
    print(기본매개변수A, 기본매개변수B)


function(1, 2, 3, 4, 5, 6, 7, 8, 10, 기본매개변수A=11)
# 기본매개변수를 호출 시 불러주지 않으면 일반 매개변수 뒤의 값들은 모두 가변매개변수로 처리된다.
# 직접 이런 함수를 만들 일이 많지는 않으나, 어떠한 함수를 사용할 때(IDE,레퍼런스 볼 때) 이해해야할 일이 있으므로 알아둬야 한다.

# 튜플의 사용
for i, v in enumerate([1, 2, 3]):
    print(i, v)

# dictionary의 키
'''
a = {
    숫자형: O,
    문자형: O,
    bool: O,
    리스트: X,
    튜플: O
}
'''
a = {
    (0, 0): 10,
    (0, 1): 20
}
print(a[0, 0])  # 그래서 이런 코드도 가능하다.(데이터분석 시 많이 사용)

# 콜백함수


def call_10_times(func):
    for i in range(10):
        # 콜백함수
        func(i)


def print_hello(num):
    print('hello', num)


# call_10_times(print_hello)

# 람다
call_10_times(lambda num: print('hello', num))

# filter


def 짝수만(number):
    return number % 2 == 0  # bool이 와야한다.


a = list(range(100))
b = filter(짝수만, a)
print(list(b))
# filter - 람다
c = filter(lambda number: number % 2 == 0, a)
print(list(c))

# map


def 제곱(number):
    return number * number


# print(list(map(제곱, a)))
# 람다
print(list(map(lambda number: number * number, a)))

# 리스트 내포 -> 새로운 리스트, 메모리 사용
print([i * i for i in a if i % 2 == 0])
# map, filter -> 제너레이터
