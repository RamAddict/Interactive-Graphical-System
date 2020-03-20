"""A custom implementation of some Basic Linear Algebra Subprograms (BLAS)."""

from typing import Iterable, Union


class Vector:
    def __init__(self, x, y, *coordinates):
        self._coordinates = [x, y] + list(coordinates)

    def __getitem__(self, key):
        return self._coordinates[key]

    def __setitem__(self, key, item):
        self._coordinates[key] = item

    def __len__(self):
        return len(self._coordinates)

    def __repr__(self):
        return "(%s)" % str(self._coordinates)[1:-1]

    def __add__(self, other: Iterable):
        try:
            small, big = sorted((self, other), key=len)
            limit = len(small)
            v = (x + small[i] if i < limit else x for i, x in enumerate(big))
            return Vector(*v)
        except BaseException as exc:
            raise NotImplementedError from exc

    def __radd__(self, other):
        return self + other

    def __sub__(self, other: Iterable):
        return self + tuple(-x for x in other)

    def __rsub__(self, other):
        return other + (-self)

    def __mul__(self, other: Union[Iterable, int, float, complex]):
        if isinstance(other, (int, float, complex)):  # scalar product
            return Vector(*(x * other for x in self))
        else:  # dot product
            try:
                dim = min(len(self), len(other))
                return sum(self[i] * other[i] for i in range(dim))
            except BaseException as exc:
                raise NotImplementedError from exc

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return self * -1

    def __truediv__(self, scalar):
        return self * 1/scalar

    def __mod__(self, z):
        return Vector(*(x % z for x in self))

    def __lshift__(self, k: int):
        return Vector(*(self[k:] + self[:k]))

    def __rshift__(self, k: int):
        return Vector(*(self[-k:] + self[:-k]))

    # @TODO: matrix multiplication (operator @)
    # def __matmul__(self, other):
    #     pass
    #
    # def __rmatmul__(self, other):
    #     pass

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, x):
        self[0] = x

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, y):
        self[1] = y

    @property
    def z(self):
        return self[2]

    @z.setter
    def z(self, z):
        self[2] = z
