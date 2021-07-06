from typing import Dict, Tuple
from graphics import Drawable, Point, Line, Wireframe


class ObjDescriptor:
    """Class for Writing .obj files"""
    def __init__(self, display_file: Dict[str, Drawable]):
        self.display_file = display_file
        self.counter = 0

    def reset_counter(self):
        self.counter = 0

    def write_obj(self, object_name: str, reset_counter=False) -> Tuple:
        """
        first string is list of vertices, second string is rest of object details
        returns Tuple(a, b) where a is the vertices and b is the structure.
        The return is ready to be written to a file
        """
        if reset_counter:
            self.reset_counter()
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

    def read_obj_file(self, path: str) -> Dict[str, Drawable]:
        line_to_point_map = [None]
        file = open(path, "r")
        for line in file.readlines():
            line_array = line.strip("\n").split(" ")
            if line_array[0] == 'v':
                line_to_point_map.append(Point(float(line_array[1]), float(line_array[2])))
            elif line_array[0] == 'o':
                object_name = line_array[1]
                self.display_file[object_name] = Drawable()
            # elif line_array[0] == 'usemtl':
                # object_color = line_array[1]
                # self.display_file[object_name].color = object_color
            elif line_array[0] == 'p':
                self.display_file[object_name] = line_to_point_map[int(line_array[1])]
            elif line_array[0] == 'l' or line_array[0] == 'f':
                if len(line_array[1:]) > 2:
                    self.display_file[object_name] = Wireframe(*[line_to_point_map[int(p)] for p in line_array[1:]])
                else:
                    self.display_file[object_name] = Line(*[line_to_point_map[int(p)] for p in line_array[1:]])
        return self.display_file
