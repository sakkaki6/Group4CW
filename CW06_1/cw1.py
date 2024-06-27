class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

   

book1 = Book("ask", "elif safak", 2009)
print(book1.title)
print(book1.author)
print(book1.published_year)
