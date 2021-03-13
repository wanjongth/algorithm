a = [1, 2, 3, 4]
b = a
print(id(b)-id(a))

a[1] = 4
print(a)
print(b)

c = a[:]  # from copy import copy -> c = copy(a) 와 같다
a[1] = 2
print(a)
print(c)
