
from typing import Dict
from graphics import Drawable


class ObjDescriptor:
    """Class for Writing .obj files"""
    def __init__(self, display_file: Dict[str, Drawable]):
        self.display_file = display_file
        # file.write("# List of vertices:")

    def write_obj(self, file_name: str, object: str):
        file = open(file_name, 'a')
        for point in self.display_file[object]:
            file.write("v " + str(point.x) + " " + str(point.y) + " 1.0 1.0\n")

    def write_all_display_file(self, file_name: str):
        file = open(file_name, 'w')
        file.write("# List of geometric vertices, with (x, y, z [,w]) coordinates, w is optional and defaults to 1.0.\n")
        
        # insert vertices
        for obj in self.display_file.values():
            self.write_obj(file_name, obj)
        
        file.close()