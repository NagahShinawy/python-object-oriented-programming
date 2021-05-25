"""
created by Nagaj at 25/05/2021
"""


# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects

class Author:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}".title()


class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    @property
    def get_book_page_count(self):
        return sum([chapter.chpagecount for chapter in self.chapters])


class Chapter:

    def __init__(self, chname, chpagecount):
        self.chname = chname
        self.chpagecount = chpagecount

    def __repr__(self):
        return f"{self.chname}:{self.chpagecount}"


john = Author("john", "james")
b1 = Book("War and Peace", 39.0, john)

b1.addchapter(Chapter("Chapter 1", 10))
b1.addchapter(Chapter("Chapter 2", 30))
b1.addchapter(Chapter("Chapter 3", 60))


print(b1.title)
print(b1.chapters)
print(b1.author)
print(b1.get_book_page_count)