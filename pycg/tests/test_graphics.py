from math import pi
from graphics import Transformation, Point, Line, Polygon


def test_transformations_center_pivot():
    p = Point(5, 4)
    t = Transformation().translate(2, 1).matrix(pivot=p.center())
    p.transform(t)
    assert p == (7, 5)

    v = Line(Point(0, 0), Point(10, 0))
    r = Transformation().rotate(pi / 2).matrix(pivot=v.center())
    v.transform(r)
    a, b = v
    assert round(a.x) == 5
    assert round(a.y) == -5
    assert round(b.x) == 5
    assert round(b.y) == 5

    rect = Polygon([Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)])
    s = Transformation().scale(4, 3).matrix(pivot=rect.center())
    rect.transform(s)
    upper_left, upper_right, lower_right, lower_left, close = rect
    assert close == upper_left
    assert upper_left == (-4, 3)
    assert upper_right == (4, 3)
    assert lower_right == (4, -3)
    assert lower_left == (-4, -3)


def test_transformations_global_pivot():
    p = Point(4, 2)
    s = Transformation().scale(-3).matrix(pivot=Point(0, 0))
    p.transform(s)
    assert p == (-12, -6)

    vertical_line = Line(Point(0, 0), Point(0, 300))
    translation_by_100 = Transformation().translate(100, 0).matrix(pivot=Point(0,0))
    vertical_line.transform(translation_by_100)
    point_a, point_b = vertical_line
    assert point_a.x == 100
    assert point_a.y == 0
    assert point_b.x == 100
    assert point_b.y == 300

    rotate_by_90 = Transformation().rotate(pi/2).matrix(pivot=Point(0,0))
    vertical_line.transform(rotate_by_90)
    point_a, point_b = vertical_line
    assert round(point_a.x) == 0
    assert round(point_a.y) == 100
    assert round(point_b.x) == -300
    assert round(point_b.y) == 100
