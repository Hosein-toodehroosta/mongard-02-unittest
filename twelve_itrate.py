"""
iterable, iterator, iteration => iterate
    __iter__, __next__
"""

class Friend:
    def __init__(self):
        self.names = ['Hosein', 'Ali', 'Amir', 'Isun']
    def __iter__(self):     # for loop
        return iter(self.names)
    def __next__(self):     # next()
        names_copy = self.names
        if names_copy:
            return names_copy.pop()
        else:
            raise StopIteration()

f = Friend()

for i in f:
    print(i)
print('-'*50)

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))