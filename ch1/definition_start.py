"""
created by Nagaj at 23/05/2021
"""


# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class

class Book:

    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def book_info(self):
        print(f"Title: {self.title}")
        print(f"Price: {self.price}")
        print(f"Author: {self.author}")


def main():
    # TODO: create instances of the class
    b1 = Book("Clean Code", "30$", "bob")
    b2 = Book("Brave New World", "50$", "james")
    b3 = Book("War and Peace", "10$", "john")
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


if __name__ == '__main__':
    main()
