"""A custom implementation of some Basic Linear Algebra Subprograms (BLAS)."""

from typing import Sequence
from math import cos, sin


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
            return Vector(*[v + other[i] for i, v in enumerate(self)])
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
            return Vector(*[scalar * x for x in self])
        except BaseException as exc:
            raise NotImplementedError from exc

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other: Sequence):  # dot product
        try:
            return sum([v * other[i] for i, v in enumerate(self)])
        except BaseException as exc:
            raise NotImplementedError from exc

    def __neg__(self):
        return self * -1

    def __truediv__(self, scalar):
        return self * (1 / scalar)

    def __mod__(self, z):
        return Vector(*[x % z for x in self])

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

    @staticmethod
    def identity(n: int):
        """Create an NxN identity Matrix."""
        rows = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(1 if j == i else 0)
            rows.append(row)
        return Matrix(*rows)

    @staticmethod
    def zeros(m: int, n: int):
        """Create an MxN Matrix filled with zeros."""
        rows = []
        for i in range(m):
            rows.append([0] * n)
        return Matrix(*rows)

    def __init__(self, first: Sequence, *rest: Sequence):
        n = len(first)
        rows = []
        for row in [first] + list(rest):
            if len(row) != n:
                raise ValueError("Matrix row length mismatch.")
            else:
                rows.append(row if isinstance(row, Vector) else Vector(*row))
        super().__init__(*rows)

    @property
    def rows(self):
        return len(self)

    @property
    def columns(self):
        return len(self[0])

    def is_square(self):
        return self.rows == self.columns

    def translated(self, tx, ty, *ts):
        """Return a new transformation with an additional translation."""
        t = Matrix.identity(self.rows)
        deltas = (tx, ty) + ts
        for i in range(t.rows - 1):
            self[i][-1] = deltas[i]  # set last column of each row with delta
        return t @ self

    def rotated(self, theta: float):
        """
        Return a new transformation with an additional rotation.
        @XXX: Only 2D rotation is implemented, so make sure matrix is 3x3.
        """
        cs, sn = cos(theta), sin(theta)
        t = Matrix([cs, -sn, 0],
                   [sn, cs,  0],
                   [0,  0,   1])
        return t @ self

    def scaled(self, sx, sy, *ss):
        """Return a new transformation with an additional scaling."""
        t = Matrix.identity(self.rows)
        scaling = (sx, sy) + ss
        for i in range(t.rows - 1):
            t[i][i] = scaling[i]
        return t @ self

    def homogenized(self, origin: Sequence):
        """Return a new version of this transformation using a new origin."""
        n = len(self)
        dx, dy = origin[0], origin[1]
        to_origin = Matrix.identity(n).translated(-dx, -dy)
        back_from_origin = Matrix.identity(n).translated(dx, dy)
        return back_from_origin @ self @ to_origin

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
