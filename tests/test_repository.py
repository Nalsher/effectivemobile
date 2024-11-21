import unittest
from unittest.mock import patch, MagicMock
from src.repositories.BookRepository import MockBookRepository
from src.entity.Book import Book
from xml.dom import NotFoundErr


class RepositoryTestCase(unittest.TestCase):

    def setUp(self):
        self.repository = MockBookRepository("mock_books.json")
        self.book = Book(book_id=1, title="Test Book", author="Author", year="2020", status="В наличии")

    @patch("builtins.open", new_callable=MagicMock)
    @patch("json.load", new_callable=MagicMock)
    def test_load_books_success(self, mock_json_load, mock_open):
        mock_json_load.return_value = [
            {"book_id": 1, "title": "Test Book", "author": "Author", "year": "2020", "status": "В наличии"}]

        self.repository._load_books()

        self.assertEqual(len(self.repository.books), 1)
        self.assertEqual(self.repository.books[0].title, "Test Book")
        self.assertEqual(self.repository.books[0].author, "Author")

    @patch("builtins.open", new_callable=MagicMock)
    @patch("json.load", new_callable=MagicMock)
    def test_load_books_file_not_found(self, mock_json_load, mock_open):
        mock_open.side_effect = FileNotFoundError

        self.repository._load_books()

        self.assertEqual(len(self.repository.books), 0)

    def test_add_book_success(self):
        self.repository.books = []
        self.repository.add_book(self.book)

        # Проверяем, что книга добавлена
        self.assertEqual(len(self.repository.books), 1)
        self.assertEqual(self.repository.books[0].title, "Test Book")

    def test_add_book_invalid_year(self):
        invalid_book = Book(book_id=2, title="Invalid Book", author="Author", year="20a0", status="В наличии")

        with self.assertRaises(ValueError):
            self.repository.add_book(invalid_book)

    def test_add_book_duplicate(self):
        self.repository.books = [self.book]
        duplicate_book = Book(book_id=1, title="Duplicate Book", author="Author", year="2021", status="В наличии")

        with self.assertRaises(ValueError):
            self.repository.add_book(duplicate_book)

    def test_delete_book_success(self):
        self.repository.books = [self.book]
        result = self.repository.delete_book(1)

        self.assertTrue(result)
        self.assertEqual(len(self.repository.books), 0)

    def test_delete_book_not_found(self):
        self.repository.books = [self.book]
        result = self.repository.delete_book(2)

        self.assertFalse(result)

    def test_change_status_available_to_taken(self):
        self.repository.books = [self.book]
        result = self.repository.change_status(1)

        # Проверяем статус
        self.assertTrue(result)
        self.assertEqual(self.repository.books[0].status, "Отдана")

    def test_change_status_taken_to_available(self):
        self.book.status = "Отдана"
        self.repository.books = [self.book]
        result = self.repository.change_status(1)

        self.assertTrue(result)
        self.assertEqual(self.repository.books[0].status, "В наличии")

    def test_find_book_by_author_success(self):
        self.repository.books = [self.book]
        found_book = self.repository.find_book(book_author="Author")

        self.assertEqual(found_book.title, "Test Book")

    def test_find_book_by_author_not_found(self):
        self.repository.books = [self.book]

        with self.assertRaises(NotFoundErr):
            self.repository.find_book(book_author="Nonexistent Author")

    def test_get_all_books(self):
        self.repository.books = [self.book]
        books = self.repository.get_all_books()

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Test Book")


if __name__ == '__main__':
    unittest.main()
