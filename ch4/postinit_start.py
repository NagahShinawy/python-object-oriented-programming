# Python Object Oriented Programming by Joe Marini course example
# Using the postinit function in data classes

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # TODO: the __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__
    # we can not write __init__ because dataclass do that.

    def __post_init__(self):
        # used to add more attributes to class that might depend on values of other attributes, so it comes later
        # with __post__init__
        # called after __init__ has finished
        self.desc = f"Book <{self.title}> by Author <{self.author}>"


# create some Book objects
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: use the description attribute

print(b2.desc)
