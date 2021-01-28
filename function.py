# 문제를 푸는 코드를 함수화하면 매우 효과적으로 풀 수 있다. 동일한 알고리즘을 반복적으로 수행해야 할 때 함수는 중요하게 사용됨

# 함수의 구조
# def 함수명(매개변수):
#     실행할 소스코드
#     return 반환 값
# 이 때 매개변수나 return 문은 조재하지 않을 수 도 있다.

def add(a, b):
    return a + b
print(add(3,7))

def add2(a, b):
    print('함수의 결과:', a + b)
add2(3,7)

# 인자 a, b를 지칭해서 각각 값을 넣을 수 있다.(이 경우, 순서가 달라도 상관없다)
def add3(a, b):
    print('함수의 결과:', a + b)
add3(b = 3, a = 7)

# 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우 - global 사용
# 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 됨

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# lambda

def add(a, b):
    return a + b
# 일반적 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))