"""
    lambda (args): manipulate (args)
"""

add = lambda x, y: x + y

print(add(2, 4))
print('-'*50)

x = [1,2,3,4,5,6,7,8,9]

def multi(i):
    return i * i

print(list(map(multi, x)))
print('-'*50)

print(list(map(lambda i: i*i, x)))
print('-'*50)

print((list(filter(lambda i: i%2 == 0, x))))
print('-'*50)

y = [(4, 'b'), (2, 'a'), (5, 'c'), (1, 'e'), (3, 'd')]

print(sorted(y, key=lambda i: i[1]))
