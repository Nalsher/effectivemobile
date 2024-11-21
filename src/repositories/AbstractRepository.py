from abc import ABC, abstractmethod
from src.entity.Book import Book
from typing import List


class BookRepositoryInterface(ABC):

    @abstractmethod
    def add_book(self, book: Book) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_book(self, book_id: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def find_book(self, book_author: str | None = None, book_id: int | None = None, book_year: str | None = None) -> Book:
        raise NotImplementedError

    @abstractmethod
    def change_status(self, book_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        raise NotImplementedError
