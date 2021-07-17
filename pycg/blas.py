"""A custom implementation of some Basic Linear Algebra Subprograms (BLAS)."""

from typing import Sequence, Callable

import numpy as np


class Matrix:
    """Matrix structured for row-major access."""

    def __init__(self, first: Sequence, *rest: Sequence):
        if isinstance(first, np.ndarray):
            self._matrix = first
        else:
            self._matrix = np.array([first] + list(rest), np.float32)

    @staticmethod
    def from_lists(rows: Sequence):
        """Creates a Matrix with the given sequence of sequences."""
        return Matrix(*rows)

    @staticmethod
    def from_function(m: int, n: int, builder: Callable):
        """
        Builds an MxN Matrix by calling a given builder function on each index
        pair (row, column) and filling its cell with the function's return.
        """
        rows = [[builder(i, j) for j in range(n)] for i in range(m)]
        return Matrix.from_lists(rows)

    @staticmethod
    def identity(n: int):
        """Create an NxN identity Matrix."""
        return Matrix.from_function(n, n, lambda i, j: 1 if j == i else 0)

    @staticmethod
    def zeros(m: int, n: int):
        """Create an MxN Matrix filled with zeros."""
        return Matrix.from_function(m, n, lambda i, j: 0)

    @property
    def rows(self):
        return len(self)

    @property
    def columns(self):
        return len(self[0])

    def __getitem__(self, key):
        return self._matrix[key]

    def __setitem__(self, key, item):
        self._matrix[key] = item

    def __len__(self):
        return len(self._matrix)

    def __repr__(self):
        return str(self._matrix)

    def __add__(self, other):
        if not isinstance(other, Matrix):
            other = Matrix(*other)
        return Matrix(self._matrix + other._matrix)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            other = Matrix(*other)
        return Matrix(self._matrix - other._matrix)

    def __rsub__(self, other):
        return other + (-self)

    def __mul__(self, scalar):  # scalar product
        return Matrix(self._matrix * scalar)

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            other = Matrix(*other)
        product = self._matrix @ other._matrix
        return product if isinstance(product, np.float32) else Matrix(product)

    def __neg__(self):
        return self * -1

    def __truediv__(self, scalar):
        return self * (1 / scalar)

    def __mod__(self, z):
        return Matrix(self._matrix % z)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            other = Matrix(*other)
        return np.array_equal(self, other)

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


class Vector(Matrix):
    """Structure which can be used as a column vector."""

    def __init__(self, x, y, *others):
        super().__init__(x, y, *others)
