# 조금 더 유연한 코드 작성을 위해 혼공파 슥슥 들으며 메모(2021.07.03 ~)

# type
print(type("123"))

# 잘 사용하지 않았었다. 문자열 find 함수
print('1234'.find('1'))  # 0
print('1234'.find('5'))  # -1
print('123412'.rfind('1'))  # 4

# bool
bool()  # True or False?\

# 빈 컨테이너 (0,0.0,"",b"",[],(),{}") = False
tests = ['', 0, 0.0, "", b"", [], (), {}]
for test in tests:
    print(bool(test))

# 저번에 정리했던 boolean 타입의 활용 때문에
number = 123
if number:  # 0이 아닐 경우,, if number != 0 -> 뭐가 좋은진 모르겠지만 개발할 때 편한건 전자인 것 같다.
    print('처리')
else:
    print('0')

# pass - 알고는 있었고, 가~~끔 봤는데, 써먹어보진 않은 것 같다.
# 아무것도 수행하지 않을 때, 코드를 작성하지 않으면 에러 발생하므로
number = 0
if number != 0:
    pass
else:
    pass
