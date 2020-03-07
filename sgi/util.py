"""Miscellaneous project utilities."""

from typing import Iterable, Sequence, Generator, Tuple
from itertools import tee


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
