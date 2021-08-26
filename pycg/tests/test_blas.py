from math import radians, sqrt
from random import randint

from blas import Vector, Matrix


def test_vector_access():
    vec = Vector(1, 2, 3)
    assert len(vec) == 3

    x, y, z = vec
    assert vec.x == x
    assert vec.y == y
    assert vec.z == z
    assert vec == (x, y, z)

    for i, v in enumerate((x, y, z)):
        assert vec[i] == v


def test_vector_algebra():
    a = Vector(1, 2, 3)
    b = Vector(1, 2, 3)
    assert a is not b
    assert a == b

    c = a + b
    assert a == c - b
    assert b == c - a
    assert c == b + a

    assert a - b == a + (-b)
    assert a - b == [0, 0, 0]

    assert c == a * 2
    assert c / 2 == a


def test_vector_dot_product():
    a = Vector(1, 3, -5)
    b = Vector(4, -2, -1)
    assert a @ b == b @ a
    assert a @ b == 3


def test_vector_normalization():
    u = Vector(1, 0)
    assert u.normalized() == u

    v = Vector(1, 2, 3)
    assert v.normalized().length == 1


def test_vector_angle():
    i = Vector(1, 0)
    j = Vector(0, 1)
    assert abs(Vector.angle(i, j) - radians(90)) < 1e-6

    v = Vector(0.5, sqrt(3)/2)
    assert abs(Vector.angle(v, i) - radians(60)) < 1e-6
    assert abs(Vector.angle(v, j) - radians(30)) < 1e-6


def test_vector_cross_product():
    a = Vector(1, 3, 4)
    b = Vector(2, 7, -5)
    assert Vector.cross(a, b) == Vector(-43, 13, 1)

    x = Vector(1, 0, 0)
    y = Vector(0, 1, 0)
    z = Vector(0, 0, 1)
    assert Vector.cross(x, y) == z
    assert Vector.cross(y, z) == x
    assert Vector.cross(z, x) == y

    u = Vector(1, 0, 0)
    v = Vector(0, 1, 0)
    n = Vector(0, 0, -1)
    assert Vector.cross(v, u) == n
    assert Vector.cross(n, v) == u
    assert Vector.cross(u, n) == v


def test_matrix_access():
    ref = [[i*j for j in range(3)] for i in range(3)]
    mat = Matrix(*ref)
    for i, row in enumerate(ref):
        for j, x in enumerate(row):
            assert mat[i][j] == x

    for i, row in enumerate(Matrix.identity(randint(2, 10))):
        for j, elem in enumerate(row):
            assert elem == (1 if i == j else 0)


def test_matrix_algebra():
    a = Matrix([1, 2],
               [3, 4])
    b = Matrix([1, 2],
               [3, 4])
    assert a is not b
    assert a == b

    c = a + b
    assert a == c - b
    assert b == c - a
    assert c == b + a

    assert a - b == a + (-b)
    assert a - b == Matrix.zeros(2, 2)

    assert c == a * 2
    assert c / 2 == a


def test_matrix_multiply():
    a = Matrix([1, 2, 3],
               [4, 5, 6])
    b = Matrix([7, 8],
               [9, 10],
               [11, 12])
    c = Matrix([58,  64],
               [139, 154])
    assert a @ b == c
    assert a @ b != b @ a

    id = Matrix.identity(2) * 1
    assert id @ c == c @ id
    assert id @ c == c


def test_matrix_transpose():
    a = Matrix([1, 2, 3],
               [4, 5, 6])
    assert a.transpose() == [[1, 4], [2, 5], [3, 6]]

    b = Matrix([7, 8],
               [9, 10],
               [11, 12])
    assert b.transpose() == [[7, 9, 11], [8, 10, 12]]

    c = Matrix([58,  64],
               [139, 154])
    assert c.transpose() == [[58, 139], [64, 154]]
