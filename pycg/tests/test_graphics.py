from math import pi

from graphics import Point, Line, Transformation


def test_transformations():
    p = Point(5, 4)
    t = Transformation().translate(2, 1)
    p.transform(t)
    assert p == (7, 5)

    v = Line(Point(0, 0), Point(10, 0))
    r = Transformation().rotate(pi / 2)
    v.transform(r)
    a, b = v
    assert round(a.x) == 5
    assert round(a.y) == -5
    assert round(b.x) == 5
    assert round(b.y) == 5

    w = Point(4, 2)
    s = Transformation().scale(-3)
    w.transform(s, pivot=Point(0, 0))
    assert w == (-12, -6)
