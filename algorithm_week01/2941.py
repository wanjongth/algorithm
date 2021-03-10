# ljes=njak
# 접근방식
words = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for word in croatia:
    words = words.replace(word, '*')

# print(words)

print(len(words))


# 코드2

# import sys

# word = sys.stdin.readline().strip()
# wordlength = len(list(word))

# alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# search = sum([word.count(s) for s in alphabet])

# result = wordlength - search
# print(result)
