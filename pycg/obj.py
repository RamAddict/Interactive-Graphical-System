import builtins
from typing import Sequence, Tuple, Dict, Generator

from graphics import Drawable, Point, Line, Wireframe


class _ObjDescriptor:
    def __init__(
        self,
        name: str,
        kind: str = None,
        vertex_indexes: Sequence[int] = None,
        attributes: Dict[str, str] = None,
    ):
        self.name = name
        self.kind = kind or None
        self.vertex_indexes = vertex_indexes or []
        self.attributes = attributes or {}


class ObjFile:
    """Python 'File-like Object' interface for Wavefront's OBJ format."""

    def __init__(self, file, mode):
        self.file = file
        self.mode = mode
        if self.mode in ('r', 'r+'):  # eager parse XXX: we don't treat errors
            self._descriptors, self.vertices, self.globals = _parse_objs(file)
        else:  # lazy write
            assert self.mode in ('w', 'w+')
            self._descriptors = []
            self.vertices = []
            self.globals = {}

    def __iter__(self) -> Generator:
        for obj in self._descriptors:
            yield self._obj_to_drawable(obj)

    def _obj_to_drawable(self, obj: _ObjDescriptor) -> Tuple[Drawable, Dict]:
        drawable: Drawable = None
        # convert vertex indexes to actual points while building drawables
        fix = lambda i: i - 1 if i > 0 else i
        if obj.kind == 'point':
            v = self.vertices[fix(obj.vertex_indexes[0])]
            drawable = Point(*v)
        elif obj.kind == 'line':
            a = self.vertices[fix(obj.vertex_indexes[0])]
            b = self.vertices[fix(obj.vertex_indexes[1])]
            drawable = Line(a, b)
        elif obj.kind == 'wireframe':
            drawable = Wireframe(
                *[self.vertices[fix(v)] for v in obj.vertex_indexes])
        # return the drawable and any extra attributes+name
        attributes = dict(obj.attributes)
        attributes['name'] = obj.name
        return drawable, attributes

    def read(self) -> Sequence[Tuple[Drawable, Dict]]:
        assert self.mode in ('r', 'r+')
        return [obj for obj in self]

    def write(self, drawable: Drawable, name: str, **kwargs):
        assert self.mode in ('w', 'w+', 'r+')
        self._descriptors.append(self._drawable_to_obj(drawable, name, **kwargs))

    def _drawable_to_obj(self, drawable: Drawable, name: str, **kwargs) -> _ObjDescriptor:
        obj = _ObjDescriptor(name=name)
        # make sure we register vertices before indexing them
        if isinstance(drawable, Point):
            obj.kind = 'point'
            self.vertices.append(Point(*drawable))
            obj.vertex_indexes = [len(self.vertices)]
        elif isinstance(drawable, Line):
            obj.kind = 'line'
            a, b = drawable
            self.vertices += [Point(*a), Point(*b)]
            n = len(self.vertices)
            obj.vertex_indexes = [n - 1, n]
        elif isinstance(drawable, Wireframe):
            obj.kind = 'wireframe'
            for p in drawable:
                self.vertices.append(Point(*p))
                obj.vertex_indexes.append(len(self.vertices))
        # use kwargs as object-local attributes
        for key, value in kwargs.items():
            obj.attributes[key] = value
        return obj

    def close(self):
        if self.mode in ('w', 'w+', 'r+') and len(self._descriptors) > 0:
            _dump_objs(self.file, self._descriptors, self.vertices, self.globals)
        return self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.mode in ('w', 'w+', 'r+') and len(self._descriptors) > 0:
            _dump_objs(self.file, self._descriptors, self.vertices, self.globals)
        return self.file.__exit__(exc_type, exc_value, traceback)

    @property
    def closed(self) -> bool:
        return self.file.closed


def open(path, mode: str = 'r'):
    if mode.lower() not in ('r', 'r+' 'w', 'w+'):
        raise ValueError("File mode should be one of 'r', 'r+', 'w' or 'w+'")
    else:
        return ObjFile(builtins.open(path, mode), mode)


def _parse_objs(file) -> Tuple[Sequence[_ObjDescriptor], Sequence[Point], Dict[str, str]]:
    descriptors: Sequence[_ObjDescriptor] = []
    vertices: Sequence[Point] = []
    extras: Dict[str, str] = {}

    current_obj = None
    for line in file:
        # skip empty lines
        words = line.strip().split()
        if not words:
            continue

        head, *body = words
        if head == '#':
            continue
        elif head == 'v':
            x, y, *_ = body
            vertices.append(Point(float(x), float(y)))
        elif head == 'o':
            if current_obj is not None:  # close obj before new ones
                descriptors.append(current_obj)
            # start a new object with partial information
            current_obj = _ObjDescriptor(name=body[0])
        elif head == 'p':
            assert current_obj is not None
            current_obj.kind = 'point'
            current_obj.vertex_indexes = [int(body[0])]
        elif head in ('l', 'f'):
            assert current_obj is not None
            current_obj.kind = 'wireframe' if len(body) > 2 else 'line'
            current_obj.vertex_indexes = [int(v) for v in body]
        elif current_obj is None:  # global config (like mtllib)
            extras[head] = body[0]
        elif current_obj is not None:  # object-local config
            current_obj.attributes[head] = body[0]

    if current_obj is not None:  # also close obj on end on file
        descriptors.append(current_obj)

    return descriptors, vertices, extras


def _dump_objs(file, descriptors: _ObjDescriptor, vertices: Sequence[Point], extras: Dict):
    # emit vertices
    for vertex in vertices:
        x, y, *z = vertex
        z = z[0] if z else 1.0
        file.write(f"v {x} {y} {z} 1.0\n")

    # emit global attributes
    for key, value in extras.items():
        file.write(f"{key} {value}\n")

    # then, emit each individual object
    for obj in descriptors:
        file.write(f"o {obj.name}\n")
        for key, value in obj.attributes.items():
            file.write(f"{key} {value}\n")
        kind = obj.kind.lower()
        if kind == 'point':
            file.write(f"p {obj.vertex_indexes[0]}\n")
        elif kind == 'line':
            a, b = obj.vertex_indexes
            file.write(f"l {a} {b}\n")
        elif kind == 'wireframe':
            file.write(" ".join(["l"] + [str(v) for v in obj.vertex_indexes]))
            file.write("\n")
