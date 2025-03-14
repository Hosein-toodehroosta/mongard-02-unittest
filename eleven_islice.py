"""
itertools.islice()
"""

from itertools import islice

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = islice(x, 2, None, 3)

print(list(result))