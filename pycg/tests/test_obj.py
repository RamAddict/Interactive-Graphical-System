from os import remove

import obj
from graphics import Line, Point, Wireframe, Polygon


def test_write_read_idempotent():
    written = {
        'test_point': Point(0, 10),
        'test_line': Line(Point(0, 22), Point(0, 310)),
        'test_polygon': Polygon([
            Point(-575, 0),
            Point(-475, 135),
            Point(-220, 152),
            Point(-130, 300),
            Point(0, 0)
        ]),
        'test_wireframe': Wireframe([
            Point(0, 0),
            Point(400, 300),
            Point(400, 0),
        ]),
    }

    with obj.open('__temp.obj', 'w+') as file:
        for name, drawable in written.items():
            file.write(drawable, name)

    with obj.open('__temp.obj') as file:
        for read, name in file:
            assert read == written[name]

    remove('__temp.obj')
