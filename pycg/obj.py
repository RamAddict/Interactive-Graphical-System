"""Custom OBJ (de)serialization for our 3D models (Wireframe and Mesh)."""

import builtins
from os import path
from typing import List, Dict, Sequence, Tuple, Generator

from graphics import Drawable, Point, Linestring, Polygon, Wireframe, Mesh, Color
from utilities import iter_no_str


class _ObjDescriptor:
    def __init__(
        self,
        name: str,
        kind: str = None,
        vertex_indexes: List[List[int]] = None,
        attributes: Dict[str, str] = None,
    ):
        self.kind = kind
        self.vertex_indexes = vertex_indexes or []
        self.attributes = attributes or {}
        self.attributes['name'] = name
        self.name = name


class ObjFile:
    """Python 'File-like Object' interface for Wavefront's OBJ format."""

    def __init__(self, file, mode, **kwargs):
        self.file = file
        self.mode = mode
        if self.mode in ('r', 'r+'):  # eager parse XXX: we don't treat errors
            self._descriptors, self._vertices, self._globals = _parse_objs(file)
        else:
            assert self.mode in ('w', 'w+')  # lazy write
            self._descriptors = []
            self._vertices = [None]
            self._globals = kwargs

    def __iter__(self) -> Generator:
        for obj in self._descriptors:
            yield self._obj_to_drawable(obj)

    def _obj_to_drawable(self, obj: _ObjDescriptor) -> Tuple[Drawable, Dict]:
        if obj.kind == 'wireframe':
            wires = []
            for wire in obj.vertex_indexes:
                points = []
                for p in wire:
                    points.append(self._vertices[p])
                wires.append(Linestring(points))
            return Wireframe(wires), obj.attributes
        elif obj.kind == 'mesh':
            faces = []
            for face in obj.vertex_indexes:
                points = []
                for p in face:
                    points.append(self._vertices[p])
                faces.append(Polygon(points))
            return Mesh(faces), obj.attributes

    def read(self) -> Sequence:
        assert self.mode in ('r', 'r+')
        return [x for x in self]

    def write(self, drawable: Drawable, name: str, **kwargs):
        assert self.mode in ('w', 'w+', 'r+')
        self._descriptors.append(self._drawable_to_obj(drawable, name, **kwargs))

    def _drawable_to_obj(self, drawable: Drawable, name: str, **kwargs) -> _ObjDescriptor:
        # handle simpler objects by converting them to either a wireframe or mesh
        if isinstance(drawable, Point):
            p = drawable
            return self._drawable_to_obj(Linestring([p, p]), name, **kwargs)
        elif isinstance(drawable, Polygon):
            face = drawable
            return self._drawable_to_obj(Mesh([face]), name, **kwargs)
        elif isinstance(drawable, Linestring):
            wire = drawable
            return self._drawable_to_obj(Wireframe([wire]), name, **kwargs)

        # make sure we register vertices before indexing them
        if isinstance(drawable, Wireframe):
            obj = _ObjDescriptor(name, 'wireframe', attributes=kwargs)
            for wire in drawable.wires:
                obj.vertex_indexes.append([])
                for point in wire:
                    self._vertices.append(Point(*point))
                    obj.vertex_indexes[-1].append(len(self._vertices) - 1)
            return obj
        elif isinstance(drawable, Mesh):
            obj = _ObjDescriptor(name, 'mesh', attributes=kwargs)
            for face in drawable.faces:
                obj.vertex_indexes.append([])
                for point in face:
                    self._vertices.append(Point(*point))
                    obj.vertex_indexes[-1].append(len(self._vertices) - 1)
            return obj

    def close(self):
        if self.mode in ('w', 'w+', 'r+') and len(self._descriptors) > 0:
            _dump_objs(self.file, self._descriptors, self._vertices, self._globals)
        return self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.mode in ('w', 'w+', 'r+') and len(self._descriptors) > 0:
            _dump_objs(self.file, self._descriptors, self._vertices, self._globals)
        return self.file.__exit__(exc_type, exc_value, traceback)

    @property
    def closed(self) -> bool:
        return self.file.closed


def open(path, mode: str = 'r', **kwargs):
    if mode.lower() not in ('r', 'r+' 'w', 'w+'):
        raise ValueError("File mode should be one of 'r', 'r+', 'w' or 'w+'")
    else:
        return ObjFile(builtins.open(path, mode), mode, **kwargs)


def _parse_objs(file) -> Tuple[Sequence[_ObjDescriptor], List[Point], Dict]:
    descriptors = []
    vertices = [None]
    globals_ = {}

    materials: Dict[str, Color] = {}

    # if we never see an 'o', assume the entire file's an object
    current_obj = _ObjDescriptor(name=path.basename(file.name).split('.')[0])
    for line in file:
        # skip empty lines
        words = line.strip().split()
        if not words: continue

        head, *body = words
        if head == '#':
            continue
        elif head == 'mtllib':
            dirname = path.dirname(path.abspath(file.name))
            for libname in body:
                globals_['mtllib'] = list(body)
                libpath = dirname + '/' + libname
                with builtins.open(libpath, 'r') as lib:
                    mtl = None
                    for line in lib:
                        words = line.strip().split()
                        if not words or head == '#':
                            continue
                        elif words[0] == 'newmtl':
                            mtl = words[1]
                        elif words[0] == 'Kd':
                            assert mtl is not None
                            color = Color(*map(lambda x: int(float(x)*0xFF), words[1:]))
                            materials[mtl] = color
                            mtl = None
        elif head == 'v':
            x, y, z, *_ = body
            x = x.split('/')[0]
            y = y.split('/')[0]
            z = z.split('/')[0]
            vertices.append(Point(float(x), float(y), float(z)))
        elif head == 'o':
            # before starting an object, we need to "finish" the current one
            if current_obj is not None and current_obj.kind is not None:
                descriptors.append(current_obj)
            # start a new object with partial information
            current_obj = _ObjDescriptor(name=body[0])
        elif head == 'usemtl':
            assert current_obj is not None
            mtl = body[0]
            current_obj.attributes['usemtl'] = mtl
            current_obj.attributes['color'] = materials[mtl]
        elif head == 'p':
            assert current_obj is not None
            current_obj.kind = 'wireframe'
            p = int(body[0].split('/')[0])
            current_obj.vertex_indexes.append([p, p])
        elif head == 'l':
            assert current_obj is not None
            current_obj.kind = 'wireframe'
            current_obj.vertex_indexes.append([])
            for v in body:
                v = v.split('/')[0]
                current_obj.vertex_indexes[-1].append(int(v))
        elif head == 'f':
            assert current_obj is not None
            current_obj.kind = 'mesh'
            current_obj.vertex_indexes.append([])
            for v in body:
                v = v.split('/')[0]
                current_obj.vertex_indexes[-1].append(int(v))
        elif head == 'w':
            assert current_obj is not None
            current_obj = None  # nope!

    if current_obj is not None:  # also close obj on end on file
        descriptors.append(current_obj)

    return descriptors, vertices, globals_


def _dump_objs(file, descriptors: Sequence[_ObjDescriptor], vertices: List[Point], globals_: Dict):
    # emit vertices
    for vertex in vertices[1:]:
        x, y, z, *_ = vertex
        file.write(f"v {x} {y} {z} 1.0\n")

    # emit global configs
    for head in globals_.keys():
        file.write(head + " ")
        for body in iter_no_str(globals_[head]): file.write(body + " ")
        file.write("\n")

    # then, emit each individual object
    for obj in descriptors:
        file.write(f"o {obj.name}\n")

        for key in obj.attributes.keys():
            if key in ('name', 'color'): continue
            file.write(key + " ")
            for val in iter_no_str(obj.attributes[key]): file.write(val + " ")
            file.write("\n")

        if obj.kind == 'wireframe':
            for wire in obj.vertex_indexes:
                file.write(" ".join(["l"] + [str(p) for p in wire]))
                file.write("\n")
        elif obj.kind == 'mesh':
            for face in obj.vertex_indexes:
                file.write(" ".join(["f"] + [str(p) for p in face]))
                file.write("\n")
