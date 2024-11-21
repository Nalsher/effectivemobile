import unittest
from src.entity.Book import Book


class EntityTestCase(unittest.TestCase):

    def stub_entity(self) -> Book:
        stub = Book(book_id=1, title="test", author="test", year="2024")
        return stub

    def test_entity_repr(self):
        stub = self.stub_entity()
        repr_format = f"Book(id={stub.book_id}, title='{stub.title}', author='{stub.author}', year='{stub.year}',status='{stub.status}')"
        assert stub.__repr__() == repr_format


if __name__ == '__main__':
    unittest.main()
