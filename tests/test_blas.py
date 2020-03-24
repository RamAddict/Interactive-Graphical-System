from random import randint
from math import pi

from pycg.blas import Vector, Matrix


tolerance = 1e-10


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
    assert a - b == (0, 0, 0)

    assert c == a * 2
    assert c / 2 == a


def test_vector_product():
    a = Vector(1, 3, -5)
    b = Vector(4, -2, -1)
    assert a @ b == a @ b
    assert a @ b == 3


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
    c = [[58,  64],
         [139, 154]]
    assert a @ b == c
    assert a @ b != b @ a


def test_matrix_transformations():
    v = Vector(5, 4, 1)
    t = Matrix.identity(3).translated(2, 1)
    assert t @ v == [7, 5, 1]

    v = Vector(10, 0, 1)
    t = Matrix.identity(3).rotated(pi / 2)
    x, y, h = t @ v
    assert h == 1
    assert abs(x - 0) < tolerance
    assert abs(y - 10) < tolerance

    v = Vector(4, 2, 1)
    t = Matrix.identity(3).scaled(-1, 3)
    assert t @ v == [-4, 6, 1]
