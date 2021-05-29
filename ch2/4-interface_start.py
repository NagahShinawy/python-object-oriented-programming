# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod


class Jsonify(ABC):

    @abstractmethod
    def to_json(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape,
             # Unfortunately, Python doesn't have interfaces
             Jsonify):  # Jsonify just like interface(options). add it when as class you need. add it as needed
    # we can implement interface in python using ABC and multiple inheritance
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def to_json(self):
        return {
            "radius": self.radius,
            "areas": self.calcArea()
        }


c = Circle(10)
print(c.calcArea())

print(c.to_json())
