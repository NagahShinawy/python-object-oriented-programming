# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects

from dataclasses import dataclass


@dataclass
class Book:
    title: str  # using type hinting (REQUIRED) for dataclass[Book] to work
    author: str
    pages: int
    __price: float
    __discount: float = 0

    def bookinfo(self):
        print(f"Title is:{self.title}")
        print(f"Author is:{self.author}")
        print(f"Pages is:{self.pages}")
        print(f"Price is:{self.__price}")

    def add_discount(self, value: float):  # use type hinting
        if 0 <= value <= 1:
            self.__discount = value
            self.__price = self.__price - (self.__price * self.__discount)
            return self.__price
        raise ValueError(f"Value of discount '{value}' is not correct")

    @property
    def price(self):
        return self.__price


# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 100.0)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
# access fields
print("Title:", b1.title)
print("Author:", b2.author)
print("Price", b1.price)
b1.add_discount(.50)
print("Price", b1.price)
# TODO: print the book itself - dataclasses implement __repr__
print(b1)
# TODO: comparing two dataclasses - they implement __eq__
print(b1 == b2)
print(b1 == b3)

# TODO: change some fields
b1.title = "clean code"
print(b1)

print(b3.price)

print("#" * 100)
b1.bookinfo()
