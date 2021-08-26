from os import remove

import obj
from graphics import Point, Linestring, Polygon, Wireframe, Mesh, Color


def test_write_read():
    written = {
        'test_point': Point(0, 10),
        'test_linestring': Linestring([Point(0, 22), Point(0, 310)]),
        'test_polygon': Polygon([
            Point(-575, 0),
            Point(-475, 135),
            Point(-220, 152),
            Point(-130, 300),
            Point(0, 0)
        ]),
        'test_wireframe': Wireframe([
            Linestring([
                Point(0, 0),
                Point(400, 300),
                Point(400, 0),
            ]),
            Linestring([
                Point(200, 0),
                Point(600, 300),
                Point(600, 0),
            ]),
        ]),
        'test_mesh': Mesh([
            Polygon([
                Point(0, -200),
                Point(400, 100),
                Point(400, -200),
            ]),
            Polygon([
                Point(200, -200),
                Point(600, 100),
                Point(600, -200),
            ]),
        ]),
    }

    read = {
        'test_point': Wireframe([Linestring([Point(0, 10), Point(0, 10)])]),
        'test_linestring': Wireframe([Linestring([Point(0, 22), Point(0, 310)])]),
        'test_polygon': Mesh([Polygon([
            Point(-575, 0),
            Point(-475, 135),
            Point(-220, 152),
            Point(-130, 300),
            Point(0, 0)
        ])]),
        'test_wireframe': Wireframe([
            Linestring([
                Point(0, 0),
                Point(400, 300),
                Point(400, 0),
            ]),
            Linestring([
                Point(200, 0),
                Point(600, 300),
                Point(600, 0),
            ]),
        ]),
        'test_mesh': Mesh([
            Polygon([
                Point(0, -200),
                Point(400, 100),
                Point(400, -200),
            ]),
            Polygon([
                Point(200, -200),
                Point(600, 100),
                Point(600, -200),
            ]),
        ]),
    }

    with open('__temp.mtl', 'w+') as file:
        file.write("newmtl mtl\n")
        file.write(f"Kd {0x01/255} {0xA1/255} {0xd0/255}\n")

    with obj.open('__temp.obj', 'w+', mtllib='__temp.mtl') as file:
        for name, drawable in written.items():
            file.write(drawable, name, usemtl='mtl')

    with obj.open('__temp.obj') as file:
        for drawable, attributes in file:
            assert drawable == read[attributes['name']]
            assert attributes['usemtl'] == 'mtl'
            assert attributes['color'] == Color(0x01, 0xA1, 0xd0)

    remove('__temp.obj')
    remove('__temp.mtl')
