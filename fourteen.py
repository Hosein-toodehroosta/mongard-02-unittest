from itertools import islice
from functools import partial


l = [1, 2, 3, 4, 5, 6, 7]

def take(iterable, n):
    return list(islice(iterable, n))

def chunked(iterable, n, strict=False):
    iteretor = iter(partial(take, iter(iterable), n), [])
    if strict:
        if n is None:
            raise ValueError("n cannot be None when strict is True")
        def ret():
            for chunk in iteretor:
                if len(chunk) != n:
                    raise ValueError("chunk is not divisible by n")
                yield chunk
        return iter(ret())
    else:
        return iteretor



