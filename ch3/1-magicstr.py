"""
created by Nagaj at 26/05/2021
"""


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string (displayed to th user)
    def __str__(self):
        return self.title

    # TODO: use the __repr__ method to return an obj representation (used for debugging, display a lot of details info )
    def __repr__(self):
        return f"{self.title} By {self.author}"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1)  # 'War and Peace' (using __str__ to display to the user
print(b2)
print(str(b1))
print("#" * 100)
print(repr(b1))  # 'War and Peace By Leo Tolstoy' (used __repr__ for more info for debugging
