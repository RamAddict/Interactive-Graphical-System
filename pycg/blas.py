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
    
    def __eq__(self, other):
        if isinstance(other, Vector) and len(self) == len(other):
            for i in range(len(self)):
                if self._coordinates[i] != other._coordinates[i]:
                    return False
            return True
        return False

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

class Matrix(Vector):
    """Basic Matrix class. The vectors of the matrix are its columns"""
    def __init__(self, vect, *columns):
        self._matrix = [vect] + list(columns)
    
    def __eq__(self, other):
        if isinstance(other, Matrix) and len(self) == len(other):
            for i in range(len(self)):
                if self._matrix[i] != other._matrix[i]:
                    return False
            # very pretty, but this returns a generator
            # x = (True if other._matrix[i] == elem else False for i, elem in enumerate(self._matrix))
            return True
        return False

    def __ne__(self, other):
        return not self == other

    def __getitem__(self, key):
        return self._matrix[key]
    
    def __setitem__(self, key, vector: Vector):
        self._matrix[key] = vector
    
    def __len__(self):
        return len(self._matrix)
    
    def __repr__(self):
        return "(%s)" % str(self._matrix)[1:-1]

    def __add__(self, other):
        dim = min(len(self), len(other))
        x = Matrix(self._matrix[0] + other._matrix[0])
        for i in range(dim)[1:]:
            x._matrix.append(self._matrix[i] + other._matrix[i])
        return x

    def __mul__(self, other):
    # @FIXME change error name
        if (len(self._matrix) != len(other[0])):
            raise NotImplementedError()
        new_matrix = []
        for p in range(len(other)):
            new_column = []
            for j in range(len(self._matrix[0])):
                sum = 0
                for i, jj in enumerate(self._matrix):
                    sum += jj[j] * other[p][i]
                new_column.append(sum)
            new_matrix.append(Vector(*new_column))
        return Matrix(*new_matrix)

    def center_point(self):
        sum = self._matrix[0]
        for vect in self._matrix[1:]:
            sum+=vect
        return sum
    
    def translate(self, vect: Vector):
        # insert coordinates into last line
        identity = self.identity(len(vect)+1)
        for j, i in enumerate(identity[:-1]):
            i[-1] = vect[j]
        return self._matrix * identity

    @staticmethod
    def identity(size: int):
        if size == 1:
            return 1
        elif size == 2:
            return Matrix(Vector(1, 0), Vector(0, 1))
        elif size == 3:
            return Matrix(Vector(1,0,0), Vector(0,1,0), Vector(0,0,1))
        elif size == 4:
            return Matrix(Vector(1,0,0,0), Vector(0,1,0,0), Vector(0,0,1,0), Vector(0,0,0,1))
        else:
            identity = []
            for i in range(size):
                column = []
                for j in range(size):
                    if i == j:
                        column.append(1)
                    else:
                        column.append(0)
                identity.append(Vector(*column))
            return Matrix(*identity)
