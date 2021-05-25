# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        # diamond problem: caused because ambiguity
        # __mro__
        self.name = "John"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Leon"


class C(A, B):
    def __init__(self):
        super().__init__()
        self.x = "x"

    def showpros(self):
        print("FOO: ", self.foo)
        print("BAR: ", self.bar)
        print("X: ", self.x)
        print("Name: ", self.name)


c = C()

print(c)

print(isinstance(c, C))
print(isinstance(c, A))
print(isinstance(c, B))

# #################

print("#" * 50)
print(hasattr(c, "foo"))
print(hasattr(c, "bar"))
print(hasattr(c, "x"))

print("#" * 50)

c.showpros()

# means find attr and methods in 'C' then 'A', then 'B' then object : lookup starts from 'C' to 'object'
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(c.__class__.__mro__)