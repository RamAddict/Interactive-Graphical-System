"""@TODO: graphics module docstrings"""

from typing import Generator, Sequence, Tuple
from itertools import tee


def grouped(seq: Sequence, n: int) -> Generator[Tuple, None, None]:
    it = iter(seq)
    return zip(*([it] * n))


def pairwise(seq: Sequence) -> Generator[Tuple, None, None]:
    return grouped(seq, 2)


def interlaced(seq: Sequence) -> Generator[Tuple, None, None]:
    first = iter(seq)
    first, second = tee(first)
    next(second)

    while True:
        try:
            yield next(first), next(second)
        except StopIteration:
            return
