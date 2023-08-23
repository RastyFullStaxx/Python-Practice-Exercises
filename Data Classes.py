from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    publication_year: int

book = Book(title='The Great Gatsby', author='F. Scott Fitzgerald', publication_year=1925)
print(book)
