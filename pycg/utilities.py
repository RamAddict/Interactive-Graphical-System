"""Miscellaneous Python utilities."""

from typing import Iterable, Sequence, Generator, Tuple
from itertools import tee
from math import log2


def grouped(iterable: Iterable, n: int) -> Generator[Tuple, None, None]:
    """Goes through an Iterable, n elements at a time.
    If there aren't enough elements left for a last iteration, it won't happen.
    """
    it = iter(iterable)
    return zip(*([it] * n))


def pairwise(seq: Sequence) -> Generator[Tuple, None, None]:
    """Goes through a Sequence, a pair at a time with repetition.
    eg: [1, 2, 3, 4, 5] -> (1, 2), (2, 3), (3, 4), (4, 5)
    """
    first = iter(seq)
    first, second = tee(first)
    next(second)
    while True:
        try:
            yield next(first), next(second)
        except StopIteration:
            return


def lerp(x, in_min, in_max, out_min, out_max):
    """Linearly interpolate x in [in_min,in_max] to y in [out_min,out_max]."""
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def experp(x, in_min, in_max, out_min, out_max):
    """Interpolate from a linear to an exponential range."""
    # solving for y = a * exp(b * x), while knowing that
    # x1 = in_min -> y1 = out_min and x2 = in_max -> y2 = out_max, thus
    # y1/y2 = exp(b * x1) / exp(b * x2) = exp(b * (x1 - x2)), then taking the
    # log of both sides: log(y1/y2) = b * (x1 - x2), so we have found b.
    b = log2(out_min / out_max) / (in_min - in_max)
    # similarly for a, y1 = a * exp(b * x1) -> a = y1 / exp(b * x1)
    a = out_min / 2**(b * in_min)
    # now we plug them into the equation (PS: base 2 is probably faster than e)
    return a * 2**(b * x)


def sign(x):
    """Get the sign of a number or 0 when it is zero."""
    return x and (1, -1)[x < 0]


def begin(*expressions):
    """Scheme-inspired hack to allow for multiple expressions in lambdas."""
    return expressions[-1]

def is_float(value):
    """Input checker for float"""
    try:
        float(value)
        return True
    except:
        return False