class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def show_book(self):
        return f"title : {self.title},author :{self.author},published_year :{self.published_year}"


book1 = Book("ask", "elif safak", 2009)
print(book1.show_book())
