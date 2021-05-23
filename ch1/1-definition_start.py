"""
created by Nagaj at 23/05/2021
"""


# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


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


class Peace(Book):
    pass


def main():
    # TODO: create instances of the class
    b1 = Book("Clean Code", 30.12, "bob", 300)
    b2 = Book("Brave New World", 50.24, "james", 500)
    b3 = Book("War and Peace", 10.99, "john", 100)
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
    print(b1.setdiscount(0.10))
    print("New Price of <{}> is <{}>".format(b1, b1.getprice()))

    print(hasattr(b1, "publisher"))  # check b1 has attr named "publisher" ?
    if hasattr(b1, "title"):  # check b1 has attr named "title" ?
        print(getattr(b1, "title"))  # value of title for object b1  ==> Clean Code


if __name__ == "__main__":
    main()
