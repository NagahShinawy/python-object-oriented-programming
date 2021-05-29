# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: __getattribute__ called when an attr is retrieved. Don't
    # directly access the attr name otherwise a recursive loop is created
    # todo: VERY IMPORTANT ,CHECK DOCS
    def __getattribute__(self, attr):
        if attr == "price":
            # الى كان مفروض يحصل فى الاوريجينال
            price = super().__getattribute__("price")  # means call the original one
            # price = object.__getattribute__(self, attr)
            discount = super().__getattribute__("_discount")
            return price - (price * discount)
        return super().__getattribute__(attr)

    # TODO: __setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, key, value):
        if key == "price":
            if type(value) is not float:
                raise ValueError(f"value {value} of {key} must be float not {type(value)}")
        super().__setattr__(key, value)

    # TODO: __getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
    def __getattr__(self, item):
        raise AttributeError(f" '{item}' attribute does not belong to '{self.__class__.__name__}' class")


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
# b3 = Book("Clean Code", "Bob", 100)  # price must be float not <class 'int'>

print(b1)
print(b1.price)

# b2.price = 40  # price must be float not <class 'int'>
b2.price = 40.0
b2.price = float(40)

print(b1.nagah)

