import unittest
from unittest import mock
from xml.dom import NotFoundErr

from src.use_cases.UseCase import BookUseCase
from src.entity.Book import Book


class UseCaseTestCase(unittest.TestCase):

    def test_add_book(self):
        mock_repository = mock.Mock()
        mock_repository.add_book.return_value = None

        usecase = BookUseCase(mock_repository)
        mock_add = usecase.repository.add_book()

        self.assertEqual(mock_add, None)

    def test_add_book_failure(self):
        mock_repository = mock.Mock()
        mock_repository.add_book.return_value = "some_data"

        usecase = BookUseCase(mock_repository)
        mock_add = usecase.repository.add_book()

        self.assertNotEqual(mock_add, None)

    def test_find_book(self):
        mock_repository = mock.Mock()
        mock_repository.find_book.return_value = Book(1, "test", "test", "2024")

        usecase = BookUseCase(mock_repository)
        mock_return = usecase.repository.find_book(1)

        self.assertIsInstance(mock_return, Book)

    def test_find_book_failure(self):
        mock_repository = mock.Mock()
        mock_repository.find_book.return_value = NotFoundErr

        usecase = BookUseCase(mock_repository)
        mock_return = usecase.repository.find_book(1)

        self.assertIs(mock_return, NotFoundErr)

    def test_delete_book(self):
        mock_repository = mock.Mock()
        mock_repository.delete_book.return_value = True

        usecase = BookUseCase(mock_repository)
        mock_delete = usecase.repository.delete_book(1)

        self.assertEqual(mock_delete, True)

    def test_delete_book_failure(self):
        mock_repository = mock.Mock()
        mock_repository.delete_book.return_value = False

        usecase = BookUseCase(mock_repository)
        mock_delete = usecase.repository.delete_book(1)

        self.assertEqual(mock_delete, False)

    def test_change_status(self):
        mock_repository = mock.Mock()
        mock_repository.change_status.return_value = True

        usecase = BookUseCase(mock_repository)
        mock_change = usecase.repository.change_status(1)

        self.assertEqual(mock_change, True)

    def test_change_status_failure(self):
        mock_repository = mock.Mock()
        mock_repository.change_status.return_value = False

        usecase = BookUseCase(mock_repository)
        mock_change = usecase.repository.change_status(1)

        self.assertEqual(mock_change, False)

    def test_list_books(self):
        mock_repository = mock.Mock()
        mock_repository.list_books.return_value = list()

        usecase = BookUseCase(mock_repository)
        mock_list_books = usecase.repository.list_books()

        self.assertEqual(mock_list_books, [])


if __name__ == '__main__':
    unittest.main()
