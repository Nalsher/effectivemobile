from src.repositories.AbstractRepository import BookRepositoryInterface
from src.entity.Book import Book
from typing import List


class BookUseCase:
    def __init__(self, repository: BookRepositoryInterface):
        self.repository = repository

    def add_book(self, book_id: int, title: str, author: str, year: str) -> None:
        new_book = Book(book_id, title, author, year)
        self.repository.add_book(new_book)

    def find_book(self, book_author: str | None = None, book_id: int | None = None, book_year: str | None = None) -> Book:
        return self.repository.find_book(book_author, book_id, book_year)

    def delete_book(self, book_id: int) -> bool:
        return self.repository.delete_book(book_id)

    def change_status(self, book_id: int) -> bool:
        return self.repository.change_status(book_id)

    def list_books(self) -> List[Book]:
        return self.repository.get_all_books()
