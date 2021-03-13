# 문자열 포매팅

# 기본 - 문자열 안에 %d, %s와 같은 포맷코드 쓰고, 뒤에 % 3, "five" 와 같은 값 입력
string = "I eat %d apples." % 3
string = "I eat %s apples." % 'five'

# 위처럼 값을 대입해도, 아래처럼 변수에 담아서 호출해도 상관 없다.
number = 3
string = "I eat %s apples." % number
# print(string)

# 두 개 이상 값을 넣을때는 간단히 괄호로 표현해주면 된다.
day = "three"
string = " I ate %d apples. so I was sick for %s days." % (number, day)
# print(string)

# 정렬과 공백
string = "%10s" % "hi"  # 앞 쪽에 공백(10 - len('hi') = 8)
string = "%-10s" % "hi"  # 뒤쪽에 공백
# print(string)

# 소수점 표현
string = "%0.4f" % 3.4213213  # 소수점 4째자리.
string = "%10.4f" % 3.4213213  # 오른쪽 정렬, 소수점 4째자리.

# 포맷함수 사용 - 간단히 문자열 뒤에 .format을 붙여준다
# 여기서 {0} <- 인덱스
string = "I eat {0} apples".format(3)  # 문자열도 바로 대입 가능
number = 3
string = "I eat {0} apples".format(number)  # 변수 대입 가능
# 여기서도 두 개이상 값을 넣을때는 간단히 괄호로 표현
string = "I ate {0} apples. so I was sick for {1} days.".format(number, day)

# 이름으로 넣기(위와 혼용 가능)
string = "I ate {number} apples. so I was sick for {day} days.".format(
    number=10, day=3)

# f 문자열 포매팅
# 변수 값을 생성한 뒤 그 값 참조 가능, 표현식 지원
name = '홍길동'
age = 30
# print(f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.')

# 딕셔너리 이용, 포매팅 변수안에는 큰따옴표("") 작은따옴표는 syntax error
d = {'name': '홍길동', 'age': 30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
