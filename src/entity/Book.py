

class Book:
    def __init__(self, book_id: int, title: str, author: str, year: str, status: str = 'В наличии'):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __repr__(self):
        return f"Book(id={self.book_id}, title='{self.title}', author='{self.author}', year='{self.year}',status='{self.status}')"
