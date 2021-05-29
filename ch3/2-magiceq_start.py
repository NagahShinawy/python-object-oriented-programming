# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):
        return f"{self.title}-{self.price}"
    # TODO: the __eq__ method checks for equality between two objects

    def __eq__(self, other):
        self.validated_parmas(other)
        # return all([self.title == other.title, self.author == other.author, self.price == other.price])
        return self.title == other.title and self.author == other.author and self.price == other.price

    # TODO: the __ge__ establishes >= relationship with another obj

    def __gt__(self, other):
        self.validated_parmas(other)
        return self.price > other.price

    def __ge__(self, other):
        self.validated_parmas(other)
        return self.price >= other.price

    def __lt__(self, other):
        self.validated_parmas(other)
        return self.price < other.price

    def __le__(self, other):
        self.validated_parmas(other)
        return self.price <= other.price

    def validated_parmas(self, other):
        if not isinstance(other, Book):  # if other.__class__ is not self.__class__:
            raise ValueError(f"Can not compare '{self.__class__.__name__}' with '{other.__class__.__name__}'")
        return other


# TODO: the __lt__ establishes < relationship with another obj


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality

print(b1 == b3)  # False: before magic method __eq__, because comparing diff instances at diff memory location
print(b1 == b3)  # True: after magic method __eq__
# print(b1 == "test")  # Value error

# TODO: Check for greater and lesser value
print("#" * 100)
print(b1 > b2)
print(b1 > b3)
print(b1 >= b3)
print(b1 < b2)
print(b3 <= b2)
print(b4 < b2)
# TODO: Now we can sort them too

books = [b1, b2, b3, b4]

print(sorted(books))  # sort func uses < operator to perform sort, we use __lt__ , so it is ok.

sorted_books = sorted(books)

print([book.title for book in sorted_books])

rev_books = sorted_books[::-1]

print(rev_books)