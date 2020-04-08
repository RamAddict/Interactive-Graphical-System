"""A custom implementation of some Basic Linear Algebra Subprograms (BLAS)."""

from typing import Sequence, Callable


class Vector:
    """Structure which can be used as a column vector."""

    def __init__(self, x, y, *others):
        self._coordinates = [x, y] + list(others)

    def __getitem__(self, key):
        return self._coordinates[key]

    def __setitem__(self, key, item):
        self._coordinates[key] = item

    def __len__(self):
        return len(self._coordinates)

    def __repr__(self):
        return str(self._coordinates)

    def __add__(self, other: Sequence):
        try:
            return Vector(*tuple(v + other[i] for i, v in enumerate(self)))
        except BaseException as exc:
            raise NotImplementedError from exc

    def __radd__(self, other):
        return self + other

    def __sub__(self, other: Sequence):
        return self + tuple(-x for x in other)

    def __rsub__(self, other):
        return other + (-self)

    def __mul__(self, scalar):  # scalar product
        try:
            return Vector(*tuple(scalar * x for x in self))
        except BaseException as exc:
            raise NotImplementedError from exc

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other: Sequence):  # dot product
        try:
            return sum(tuple(v * other[i] for i, v in enumerate(self)))
        except BaseException as exc:
            raise NotImplementedError from exc

    def __neg__(self):
        return self * -1

    def __truediv__(self, scalar):
        return self * (1 / scalar)

    def __mod__(self, z):
        return Vector(*tuple(x % z for x in self))

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i, v in enumerate(self):
            if v != other[i]:
                return False
        return True

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


class Matrix(Vector):
    """Matrix structured for row-major access."""

    def __init__(self, first: Sequence, *rest: Sequence):
        convert = lambda seq: seq if isinstance(seq, Vector) else Vector(*seq)
        n = len(first)
        rows = [convert(first)]
        for row in rest:
            if len(row) != n:
                raise ValueError("Matrix row length mismatch.")
            else:
                rows.append(convert(row))
        super().__init__(*rows)

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

    def is_square(self):
        return self.rows == self.columns

    def __matmul__(self, other):
        if isinstance(other, Matrix):
            m, n, p = self.rows, self.columns, other.columns
            if other.rows != n:
                raise ValueError("Matrix has incompatible dimensions.")
            result = Matrix.zeros(m, p)
            for i in range(m):
                for j in range(p):
                    for k in range(n):
                        result[i][j] += self[i][k] * other[k][j]
            return result
        elif isinstance(other, Vector):
            n = len(other)
            if n != self.columns:
                raise ValueError("Vector has incompatible dimensions.")
            return Vector(*[line @ other for line in self])
        else:
            raise NotImplementedError("Can't multiply Matrix by %s." %
                                      type(other).__name__)
