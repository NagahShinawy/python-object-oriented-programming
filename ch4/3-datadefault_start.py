# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field

from _factory import generate_random_number


@dataclass
class Book:
    # you can define default values when attributes are declared
    # author: str = "No Author"
    author: str
    pages: int = 0
    price: float = field(default=0.0)
    title: str = "No Title"

    def to_json(self):
        return {
            "title": self.title,
            "pages": self.pages,
            "price": self.price,
            "author": self.author,
        }


@dataclass
class Response:
    code: int = field(default=200)
    details: dict = field(
        default_factory={"ok": True}
    )  # ValueError: mutable default <class 'dict'> for field details is not allowed: use default_factory
    # so we use default_factory instead of default
    errors: dict = field(default=None)


@dataclass
class Number:
    num: int = field(
        default_factory=generate_random_number
    )  # use default_factory argument with function that return your default value
    is_even: bool = field(default=True)

    def __post_init__(self):
        # change number status to False if it is odd
        if self.num % 2 != 0:
            self.is_even = False


book = Book(author="james", pages=10)
book2 = Book(author="john", pages=200)
book3 = Book(author="leon", pages=200)
print(book)

not_found = Response(code=404, details={"msg": "page not found"})
ok = Response(code=200, details={"data": [book, book2, book3]})

print(not_found.details)
print(ok.details)
authors = [book.author for book in ok.details["data"]]

print(authors)
books = [book.to_json() for book in ok.details["data"]]

print(books)
print("#" * 100)

n = Number()
print(n)