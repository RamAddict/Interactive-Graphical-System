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
    a = Matrix(Vector(1, 0, 20.0), Vector(0, 1, 0.0), Vector(0, 0, 1.0))
    b = Matrix(Vector(80,135,0))
    c = Matrix(Vector(80,135,1600))
    assert a * b == c


def test_matrix_identity():
    a = Matrix.identity(2)
    assert a == Matrix(Vector(1,0), Vector(0, 1))
    assert Matrix.identity(5) == Matrix(Vector(1, 0, 0, 0, 0), Vector(0, 1, 0, 0, 0), 
    Vector(0, 0, 1, 0, 0), Vector(0, 0, 0, 1, 0), Vector(0, 0, 0, 0, 1))

def test_matrix_translate():
    a = Matrix.identity(3)
    a = a.translate(Vector(2, 3))
    assert a == Matrix(Vector(1, 0, 2), Vector(0, 1, 3), Vector(0, 0, 1))
