from functools import partial, update_wrapper

def multi(x, y):
    """
    multi function
    """
    return x * y


double = partial(multi, y=2)
triple = partial(multi, y=3)

print(double(8))
print(triple(8))

# print(double.__name__)    AttributeError
# print(double.__doc__)     partial(func, *args, **keywords) - new function with partial application

update_wrapper(double, multi)
print(double.__name__)
print(double.__doc__)