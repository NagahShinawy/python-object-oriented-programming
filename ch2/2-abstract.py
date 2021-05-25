"""
created by Nagaj at 25/05/2021
"""
from abc import ABC, abstractmethod
from math import pi


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"<obj> from class <{self.__class__.__name__}>"

    @abstractmethod
    def calc_area(self):
        # we need to force every shape that inherit to implement calcArea because every shape has area.
        # implement at subclasses based on shape it self, ex: Square : side * side
        # abstract methods: need to override it at subclass
        # enforce subclass to override abstract method(s)
        pass

    def show_info(self):  # every subclass can call it
        return self


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return self.radius ** 2 * pi


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calc_area(self):
        return self.side ** 2


# error TypeError: Can't instantiate abstract class GraphicShape with abstract methods calc_area
# but error just when class contains abstract method(s)
# g = GraphicShape()
c = Circle(10)
print(c.calc_area())
print(c.show_info())

# #####################################
print("#" * 50)
s = Square(12)
print(s.calc_area())
print(s.show_info())