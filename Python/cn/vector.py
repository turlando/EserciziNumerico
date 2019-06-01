from math import sqrt


def norm_1(v):
    """
    >>> norm_1((12, -5))
    17
    """
    return sum(abs(x) for x in v)


def norm_2(v):
    """
    >>> norm_2((12, -5))
    13.0
    """
    return sqrt(sum(x ** 2 for x in v))


def norm_inf(v):
    """
    >>> norm_inf((12, -5))
    12
    """
    return max(abs(x) for x in v)
