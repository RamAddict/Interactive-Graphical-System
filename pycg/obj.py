
from typing import Dict, Tuple
from graphics import Drawable, Point, Line, Wireframe


class ObjDescriptor:
    """Class for Writing .obj files"""
    def __init__(self, display_file: Dict[str, Drawable]):
        self.display_file = display_file
        self.counter = 0; 
        # file.write("# List of vertices:")

    def reset_counter(self):
        self.counter = 0;

    def write_obj(self, object_name: str, reset_counter=False) -> Tuple:
        """
        first string is list of vertices, second string is rest of object details
        returns Tuple(a, b) where a is the vertices and b is the structure.
        The return is ready to be written to a file
        """
        if reset_counter:
            self.reset_counter();
        drawable = self.display_file[object_name]
        vertices = ""
        old_counter = self.counter +1
        if type(drawable) is Point:
                vertices += ("v " + str(drawable.x) + " " + str(drawable.y) + " 0.0 1.0\n")
                self.counter+=1
        else:
            for point in drawable:
                vertices += ("v " + str(point.x) + " " + str(point.y) + " 0.0 1.0\n")
                self.counter+=1

        # define relevant attributes on the vertex (structure)
        structure = "o " + object_name + "\n"
        if type(drawable) is Point:
            structure += "p " + str(self.counter) + "\n"
        if type(drawable) is Line:
            structure += "usemtl purple\n"
            structure += "l " + str(old_counter) + " " + str(self.counter) + "\n"
        if type(drawable) is Wireframe:
            structure += "usemtl purple\n"
            append_str = "l"
            for i in range(old_counter, self.counter+1):
                append_str += " " + str(i)
            append_str += " " + str(old_counter) + "\n"
            structure += append_str

        return (vertices, structure)

    def write_all_display_file(self, file_name: str):
        if file_name == "" or file_name == "." or file_name == "..":
            file_name = "output.obj"
        else:
            file_name += ".obj"
        self.reset_counter()
        vertices = ""
        structure = ""
        for key in self.display_file.keys():
            (v,s) = self.write_obj(key)
            vertices += v
            structure += s
        file = open(file_name, 'w')
        file.write(vertices)
        file.write(structure)
        
        file.close()