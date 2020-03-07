
class Drawable:
    def draw(self):
        raise NotImplementedError()

class Shape:
    def __init__(self, name):
        self.name = name
    def name(self):
        return self.name

class Point(Shape):
    def __init__(self, name, position):
        Shape.__init__(self, name)
        self.position = position

class Line(Shape):
    def __init__(self, name, begin, end):
        Shape.__init__(self, name)
        self.line = (begin, end)

class Wireframe(Shape):
    def __init__(self, name, lines):
        Shape.__init__(self, name)
        self.lines = lines
