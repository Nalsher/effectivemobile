import os
from xml.dom import NotFoundErr
from src.repositories.BookRepository import MockBookRepository
from src.use_cases.UseCase import BookUseCase


def console_interface():
    file_path = os.path.join("../storage/books.json")
    repository = MockBookRepository(file_path)
    use_case = BookUseCase(repository)

    while True:
        print("\n=== Book Management ===")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. List All Books")
        print("4. Find Book")
        print("5. Change Book Status")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Book Author: ")
                year = input("Enter Book Year: ")
                use_case.add_book(book_id, title, author, year)
                print("Book added successfully.")
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "2":
            try:
                book_id = int(input("Enter Book ID to delete: "))
                if use_case.delete_book(book_id):
                    print("Book deleted successfully.")
                else:
                    print("Book not found.")
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "3":
            books = use_case.list_books()
            if books:
                print("\nCurrent Books:")
                for book in books:
                    print(book)
            else:
                print("No books available.")
        elif choice == "4":
            try:
                title = input("Enter Book Title: ")
                author = input("Enter Book Author: ")
                year = input("Enter Book Year: ")
                print(use_case.find_book(author, title, year))
            except NotFoundErr:
                print("Book not found")
        elif choice == "5":
            try:
                id = int(input("Enter Book ID: "))
                if (use_case.change_status(id)):
                    print("Book status changed successfuly")
                else:
                    print("Book not found")
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


console_interface()
