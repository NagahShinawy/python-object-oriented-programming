"""
created by Nagaj at 23/05/2021
"""

# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions
books = [
    {"title": "clean code", "price": 30.12, "author": "bob", "pages": 300},
    {"title": "Brave New World", "price": 50.24, "author": "james", "pages": 500},
    {"title": "War and Peace", "price": 10.99, "author": "john", "pages": 100},
    {"title": "django for web apps", "price": 15.99, "author": "open source", "pages": 1200},

]


# TODO: create a basic class


class Book:

    # the "init" function is called when the instance is
    # created and ready to be initialized

    def __init__(self, title, price, author, pages):
        # instance attr: unique for each instance(obj)
        self.title = title
        self.price = price
        self.author = author
        self.pages = pages
        self._discount = 0
        self.__private = "private"

    def __str__(self):
        return f"{self.title} By {self.author}"

    # TODO: create instance methods
    # instance methods are defined like any other function, with the
    # first argument as the object ("self" is just a convention)
    def getprice(self):
        return self.price - (self.price * self._discount)

    def setdiscount(self, amount):
        self._discount = amount

    def book_info(self):
        print(f"Title: {self.title}")
        print(f"Price: ${self.price}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


class Ebook(Book):

    def change_private(self):
        # print(self.__private)  # error name mangling
        self._Book__private = "I can change it"
        print(self._Book__private)


class Newspaper:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


def main():
    # TODO: create instances of the class
    instances = [Book(**book) for book in books]
    b1, b2, b3, b4 = instances
    print(b1)
    b1.book_info()  # Book.book_info(b1)
    # TODO: print the class and property
    print("#" * 50)
    # print(b1.title)
    # print(b1.price)
    # print(b1.author)
    b1.book_info()

    print("#" * 50)
    b2.book_info()

    print("#" * 50)
    b3.book_info()

    # TODO: print the price of book1
    print("*" * 50)
    print(b1.getprice())

    # TODO: try setting the discount
    b1.setdiscount(0.10)
    print("New Price of <{}> is <{}>".format(b1, b1.getprice()))

    print(hasattr(b1, "publisher"))  # check b1 has attr named "publisher" ?
    if hasattr(b1, "title"):  # check b1 has attr named "title" ?
        print(getattr(b1, "title"))  # value of title for object b1  ==> Clean Code

    # TODO: properties with double underscores are hidden by the interpreter
    print(b1.__dict__)
    print(b1._discount)  # it works, attr name not changed by interpreter, (protected not private)
    # print(b1.__private)  # error
    # (name of attr is changed to <_class__attr>: "_Book__private"
    # but still you can access it, private in python is just convention
    print(b1._Book__private)  # Name mangling
    b1._Book__private = 10000000
    print(b1._Book__private)   # changed
    eb = Ebook(b4.title, b4.price, b4.author, b4.pages)
    eb.change_private()

    # TODO: use type() to inspect the object type
    times = Newspaper(name="TIMES")
    print(times, type(times))

    if isinstance(times, Newspaper):
        print(f"<{times}> is instance of <{Newspaper.__name__}>")

    if not isinstance(times, Book):
        print(f"<{times}> is NOT instance of <{Book.__name__}>")

    print(times.__class__)  # <class '__main__.Newspaper'>

    print(type(eb))  # <class '__main__.Ebook'>

    print(isinstance(eb, Ebook))   # True  Ebook is subclass

    print(isinstance(eb, Book))  # True Book is superclass

    # TODO: compare two types together

    print(type(b1) == type(b2))   # True
    print(type(b1) == type(times))  # False
    print("#" * 50)
    # TODO: use isinstance to compare a specific instance to a known type

    print(isinstance(b2, Book))   # True
    print(isinstance(b2, Ebook))  # False
    print(isinstance(b2, Newspaper))  # True
    print(isinstance(b2, object))  # True

    print(b2.__class__.__mro__)   # (<class '__main__.Book'>, <class 'object'>)


if __name__ == "__main__":
    main()
