from math import pi

from graphics import Transformation, Point, Linestring, Polygon, Bezier, bezierSurface, bSplineSurface


def test_transformations_center_pivot():
    p = Point(5, 4)
    t = Transformation().translate(2, 1).matrix(pivot=p.center())
    p.transform(t)
    assert p == (7, 5)

    v = Linestring([Point(0, 0), Point(10, 0)])
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
    s = Transformation().scale(-3).matrix()
    p.transform(s)
    assert p == (-12, -6)

    vertical_line = Linestring([Point(0, 0), Point(0, 300)])
    translation_by_100 = Transformation().translate(100, 0).matrix()
    vertical_line.transform(translation_by_100)
    point_a, point_b = vertical_line
    assert point_a.x == 100
    assert point_a.y == 0
    assert point_b.x == 100
    assert point_b.y == 300

    rotate_by_90 = Transformation().rotate(pi/2).matrix()
    vertical_line.transform(rotate_by_90)
    point_a, point_b = vertical_line
    assert round(point_a.x) == 0
    assert round(point_a.y) == 100
    assert round(point_b.x) == -300
    assert round(point_b.y) == 100


# TODO: unittest clipping algos


def test_bezier():
    curve = Bezier([Point(1,1), Point(2,2), Point(3,2), Point(4,1)], step=0.1)
    correct = [Point(1.0, 1.0), Point(1.2999999523162842, 1.2699999809265137), Point(1.600000023841858, 1.4800000190734863), Point(1.9000000953674316, 1.6299999952316284), Point(2.1999998092651367, 1.71999990940094), Point(2.5, 1.75), Point(2.799999713897705, 1.7199996709823608), Point(3.0999999046325684, 1.6299998760223389), Point(3.4000000953674316, 1.4800002574920654), Point(3.6999998092651367, 1.269999623298645), Point(4.0, 1.0)]
    for actual, expected in zip(curve, correct):
        assert abs(actual.x - expected.x) < 1e-6
        assert abs(actual.y - expected.y) < 1e-6


# TODO: unittest bsplines


def test_surface_bezier():
    _ = bezierSurface([
        Point(0, 0, 0), Point(0, 3, 4), Point(0, 6, 3), Point(0, 10 ,0),
        Point(3, 2.5, 2), Point(2, 6, 5), Point(3, 8, 5), Point(4, 0, 2),
        Point(6, 3, 2), Point(8, 6, 5), Point(7, 10, 4.5 ), Point(6, 0, 2.5),
        Point(10, 0, 0), Point(11, 3, 4), Point(11, 6, 3), Point(10, 9, 0)
    ], step=.1)


def test_surface_bSpline():
    _ = bSplineSurface([
        Point(0, 0, 0), Point(0, 3, 4), Point(0, 6, 3), Point(0, 10 ,0),
        Point(3, 2.5, 2), Point(2, 6, 5), Point(3, 8, 5), Point(4, 0, 2),
        Point(6, 3, 2), Point(8, 6, 5), Point(7, 10, 4.5 ), Point(6, 0, 2.5),
        Point(10, 0, 0), Point(11, 3, 4), Point(11, 6, 3), Point(10, 9, 0)
    ], step=.1)
