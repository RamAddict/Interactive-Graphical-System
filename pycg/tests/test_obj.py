from os import remove

import obj
from graphics import Line, Point, Wireframe, Polygon, Color


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

    with open('__temp.mtl', 'w+') as file:
        file.write("newmtl mtl\n")
        file.write(f"Kd {0x01/255} {0xA1/255} {0xd0/255}\n")

    with obj.open('__temp.obj', 'w+', mtllib='__temp.mtl') as file:
        for name, drawable in written.items():
            file.write(drawable, name, usemtl='mtl')

    with obj.open('__temp.obj') as file:
        for read, attributes in file:
            assert read == written[attributes['name']]
            assert attributes['usemtl'] == 'mtl'
            assert attributes['color'] == Color(0x01, 0xA1, 0xd0)

    remove('__temp.obj')
    remove('__temp.mtl')
