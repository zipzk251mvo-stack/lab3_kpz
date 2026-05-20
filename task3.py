class Renderer:
    def render_circle(self):
        pass

    def render_square(self):
        pass

    def render_triangle(self):
        pass

class VectorRenderer(Renderer):
    def render_circle(self):
        print("Drawing Circle as vectors")

    def render_square(self):
        print("Drawing Square as vectors")

    def render_triangle(self):
        print("Drawing Triangle as vectors")

class RasterRenderer(Renderer):
    def render_circle(self):
        print("Drawing Circle as pixels")

    def render_square(self):
        print("Drawing Square as pixels")

    def render_triangle(self):
        print("Drawing Triangle as pixels")

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        self.renderer.render_circle()

class Square(Shape):
    def draw(self):
        self.renderer.render_square()

class Triangle(Shape):
    def draw(self):
        self.renderer.render_triangle()

if __name__ == "__main__":
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle = Circle(vector_renderer)
    circle.draw()

    triangle = Triangle(raster_renderer)
    triangle.draw()

    square = Square(vector_renderer)
    square.draw()