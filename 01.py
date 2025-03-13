# Learning doctest
# python -m doctest -v 01.py

""""
>>> add(5, 6)
11
>>> subtract(7, 6)
1
>>> multiply(5, 4)
20
"""

def add(x, y):
    """
    >>> add(5, 7)
    12
    >>> add(4, -1)
    3
    >>> add(0, -5)
    -5
    """
    return x + y

def subtract(x, y):
    """
    >>> subtract(5, 4)
    1
    >>> subtract(6, 9)
    -3
    """
    return x - y

def multiply(x, y):
    """
    >>> multiply(5, 6)
    30
    >>> multiply(5, 'b')
    'bbbbb'
    """
    return x * y