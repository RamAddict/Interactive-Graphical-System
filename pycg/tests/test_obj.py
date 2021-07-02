# import os, sys

# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)



from graphics import Line, Point, Wireframe
from obj import ObjDescriptor


def test_write():
    obj = ObjDescriptor({"stop": Line(Point(0, 22), Point(0, 310))})
    write = obj.write_obj("stop")
    assert write[0] == "v 0 22 0.0 1.0\nv 0 310 0.0 1.0\n"
    assert write[1] == "o stop\nusemtl purple\nl 1 2\n"

    obj = ObjDescriptor({"dude,STOP": Wireframe(Point(-575, 0),
                                Point(-475, 135),
                                Point(-220, 152),
                                Point(-130, 300),
                                Point(0, 0))})
    write = obj.write_obj("dude,STOP")
    assert write[0] == 'v -575 0 0.0 1.0\nv -475 135 0.0 1.0\nv -220 152 0.0 1.0\nv -130 300 0.0 1.0\nv 0 0 0.0 1.0\n'
    assert write[1] == 'o dude,STOP\nusemtl purple\nl 1 2 3 4 5 1\n'

    many_objs = ObjDescriptor({"dude,STOP": Wireframe(Point(-575, 0),
                                Point(-475, 135),
                                Point(-220, 152),
                                Point(-130, 300),
                                Point(0, 0)),
                        "stop": Line(Point(0, 22), Point(0, 310)),
                        "pointer": Point(0, 10)})

    other = many_objs.write_obj("dude,STOP");
    assert obj.write_obj("dude,STOP", True) == other
    # required in the next test
    many_objs.write_all_display_file("output.obj")

def test_read_obj():
    many_objs = ObjDescriptor({"dude,STOP": Wireframe(Point(-575, 0),
                                Point(-475, 135),
                                Point(-220, 152),
                                Point(-130, 300),
                                Point(0, 0)),
                        "stop": Line(Point(0, 22), Point(0, 310)),
                        "pointer": Point(0, 10)})
    objs_read = ObjDescriptor({}).read_obj_file("output.obj")
    assert objs_read == many_objs.display_file

test_read_obj()