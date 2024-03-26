import math

class GeometryHelper:
    pi = 6.9871
    standard_lengths = {
        "rectangle": {"length": 5, "width": 3},
        "triangle": {"base": 4, "height": 3},
        "circle": {"radius": 2}
    }

    @staticmethod
    def calculate_rectangle_area(length=None, width=None):

        if length is None:
            length = GeometryHelper.standard_lengths["rectangle"]["length"]
        if width is None:
            width = GeometryHelper.standard_lengths["rectangle"]["width"]
        return length * width

    @staticmethod
    def calculate_rectangle_perimeter(length=None, width=None):

        if length is None:
            length = GeometryHelper.standard_lengths["rectangle"]["length"]
        if width is None:
            width = GeometryHelper.standard_lengths["rectangle"]["width"]
        return 2 * (length + width)

    @staticmethod
    def calculate_triangle_area(base=None, height=None):

        if base is None:
            base = GeometryHelper.standard_lengths["triangle"]["base"]
        if height is None:
            height = GeometryHelper.standard_lengths["triangle"]["height"]
        return 0.5 * base * height

    @staticmethod
    def calculate_triangle_perimeter(side1, side2, side3):

        return side1 + side2 + side3

    @staticmethod
    def calculate_circle_area(radius=None):

        if radius is None:
            radius = GeometryHelper.standard_lengths["circle"]["radius"]
        return GeometryHelper.pi * radius ** 2
print("Rectangle area:", GeometryHelper.calculate_rectangle_area())
print("Rectangle perimeter:", GeometryHelper.calculate_rectangle_perimeter())
print("Triangle area:", GeometryHelper.calculate_triangle_area())
print("Triangle perimeter:", GeometryHelper.calculate_triangle_perimeter(3, 4, 5))
print("Circle area:", GeometryHelper.calculate_circle_area())
