# 처음에 생각했던 방식인데 구현하고싶음
words = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '=']

cnt = 0

for i in words:
    if words[i] in alphabet:
        break
    elif words[i] == 'n' or 'l':
        if words[i+1] == 'j':
            continue
    elif words[i] == 'c' or 's' or 'z':
        if words[i+1] == '=' or '-':
            continue
    elif words[i] == 'd':
        if words[i+1] == '0':
            continue
        elif words[i+1] == 'z' and '=':
            continue
    cnt += 1
print(cnt)

# n, l, c, s, d 를 만났을 때 그 다음 문자도 살펴보고, 특수 크로아티아 알파벳인 경우 continue --> 글자수를 세지 않고 다음 문자로 넘어감
# 그래서 일반 문자일 때 & = - 를 만났을 때 글자수를 세줌 (cnt++)
