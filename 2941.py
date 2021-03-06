# ljes=njak
# 접근방식
words = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for word in croatia:
    words = words.replace(word,'*')

# print(words)

print(len(words))