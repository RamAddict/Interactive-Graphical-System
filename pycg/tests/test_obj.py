

from graphics import Line, Point
from obj import ObjDescriptor


def test_write_read():
    obj = ObjDescriptor({"stop": Line(Point(0, 22), Point(0, 310))})
    obj.write_obj("/home/arthur/INE5420-CG/podre.obj", "stop")
    # with read()


    #TODO Finish reading files:
        #TODO read files, deal with path issue, create window to insert name in gui