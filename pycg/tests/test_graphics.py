from math import pi
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

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

    vertical_line = Line(Point(0, 0), Point(0, 300))
    translation_by_100 = Transformation().translate(100, 0)
    vertical_line.transform(translation_by_100, Point(0,0))
    point_a, point_b = vertical_line
    assert point_a.x == 100
    assert point_a.y == 0
    assert point_b.x == 100
    assert point_b.y == 300

    rotate_by_90_around_origin = Transformation().rotate(pi/2)
    vertical_line.transform(rotate_by_90_around_origin, pivot=Point(0,0))
    point_a, point_b = vertical_line
    print(vertical_line)
    assert round(point_a.x) == 0
    assert round(point_a.y) == 100
    assert round(point_b.x) == -300
    assert round(point_b.y) == 100