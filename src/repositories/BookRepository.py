import json
from xml.dom import NotFoundErr
from src.repositories.AbstractRepository import BookRepositoryInterface
from src.entity.Book import Book
from typing import List


class MockBookRepository(BookRepositoryInterface):
    def __init__(self, json_file: str):
        self.json_file = json_file
        self._load_books()

    def _load_books(self):
        try:
            with open(self.json_file, "r") as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data]
        except FileNotFoundError:
            self.books = []

    def _save_books(self):
        with open(self.json_file, "w") as file:
            json.dump([book.__dict__ for book in self.books], file, indent=4)

    def add_book(self, book: Book) -> None:
        if len(book.year) == 4 and book.year.isdigit():
            for i in self.books:
                if i.book_id == book.book_id:
                    raise ValueError
            self.books.append(book)
            self._save_books()
        else:
            raise ValueError

    def delete_book(self, book_id: int) -> bool:
        book_to_delete = next((book for book in self.books if book.book_id == book_id), None)
        if book_to_delete:
            self.books.remove(book_to_delete)
            self._save_books()
            return True
        return False

    def change_status(self, book_id: int) -> None:
        book_to_change = next((book for book in self.books if book.book_id == book_id), None)
        if book_to_change.status == "В наличии":
            book_to_change.status = "Отдана"
            return True
        else:
            book_to_change.status = "В наличии"
            return True
        return False

    def find_book(self, book_author: str | None = None, book_title: str | None = None, book_year: str | None = None) -> Book:
        if book_author:
            book_to_get = next((book for book in self.books if book.author == book_author), None)
            if book_to_get:
                return book_to_get
            else:
                raise NotFoundErr
        if book_title:
            book_to_get = next((book for book in self.books if book.title == book_title), None)
            if book_to_get:
                return book_to_get
            else:
                raise NotFoundErr
        if book_year:
            book_to_get = next((book for book in self.books if book.year == book_year), None)
            if book_to_get:
                return book_to_get
            else:
                raise NotFoundErr
        raise NotFoundErr

    def get_all_books(self) -> List[Book]:
        return self.books
