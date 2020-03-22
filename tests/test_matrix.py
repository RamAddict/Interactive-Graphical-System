from pycg.blas import Vector, Matrix

def test_matrix_add():
    #  a   +   b   =   c
    # 1 1     4 2     5 3    
    # 2 3     0 1     2 4
    a = Matrix(Vector(1, 2), Vector(1, 3))
    b = Matrix(Vector(4, 0), Vector(2, 1))
    c = Matrix(Vector(5, 2), Vector(3, 4))
    assert b + a == c
    assert a + b == c

def test_matrix_multiply():
    a = Matrix(Vector(1, 2), Vector(1, 3))
    b = Matrix(Vector(4, 0), Vector(2, 1))
    c = Matrix(Vector(8, 2), Vector(10, 3))
    assert b * a == c
    assert a * b != c
