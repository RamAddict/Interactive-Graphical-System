"""A custom implementation of some Basic Linear Algebra Subprograms (BLAS)."""

from typing import Sequence, Callable
from math import sqrt, acos


class Vector:
    """Structure which can be used as a column vector."""

    def __init__(self, first, *rest):
        self._coordinates = [first] + list(rest)

    @staticmethod
    def angle(a, b):
        """Finds the angle between two 1st-rank vectors."""
        return acos((a @ b) / (a.length * b.length))

    @staticmethod
    def cross(a, b):
        """Computes the cross product between two 3D vectors."""
        assert(len(a) == len(b) == 3)
        return Vector((a.y * b.z - a.z * b.y),
                      -(a.x * b.z - a.z * b.x),
                      (a.x * b.y - a.y * b.x))

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
        except Exception as exc:
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
        except Exception as exc:
            raise NotImplementedError from exc

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other: Sequence):  # dot product
        try:
            return sum(tuple(v * other[i] for i, v in enumerate(self)))
        except Exception as exc:
            raise NotImplementedError from exc

    def __neg__(self):
        return self * -1

    def __truediv__(self, scalar):
        return self * (1 / scalar)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i, v in enumerate(self):
            if v != other[i]:
                return False
        return True

    def normalized(self):
        """Returns a normalized version of this vector."""
        return self / self.length

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

    @property
    def length(self):
        squared_sum = 0
        for component in self:
            if isinstance(component, Vector): component = component.length
            squared_sum += component * component
        return sqrt(squared_sum)


class Matrix(Vector):
    """Matrix structured for row-major access."""

    def __init__(self, first: Sequence, *rest: Sequence):
        convert = lambda seq: seq if isinstance(seq, Vector) else Vector(*seq)
        rows = [convert(first)]
        for row in rest:
            if len(row) != len(first):
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
        return Matrix.from_function(m, n, lambda _i, _j: 0)

    def __add__(self, other: Sequence):
        return Matrix(*(super().__add__(other)))

    def __mul__(self, scalar):
        return Matrix(*(super().__mul__(scalar)))

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

    def __str__(self) -> str:
        return "[" + ";\n".join(str(line) for line in self) + "]\n"

    @property
    def rows(self):
        return len(self)

    @property
    def columns(self):
        return len(self[0])

    def transpose(self):
        """Returns a transposed version of this matrix."""
        m, n = self.rows, self.columns
        return Matrix.from_function(n, m, lambda i, j: self[j][i])
