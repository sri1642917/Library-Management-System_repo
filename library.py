from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print("Book added successfully.")
        self.log_operation(f"Added new book with ISBN: {isbn}")

    def list_books(self):
        if self.books:
            print("\n===== List of Books =====")
            for book in self.books:
                print(book)
        else:
            print("No books available.")

    def search_book(self, keyword):
        found = False
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower() or keyword.lower() in book.isbn.lower():
                print(book)
                found = True
        if not found:
            print("Book not found.")

    def delete_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        print("Book deleted successfully.")
        self.log_operation(f"Deleted book with ISBN: {isbn}")

    def update_book_availability(self, isbn, availability):
        for book in self.books:
            if book.isbn == isbn:
                book.available = availability
                print(f"Updated availability of book with ISBN: {isbn} to {availability}")
                self.log_operation(f"Updated availability of book with ISBN: {isbn} to {availability}")
                break

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)
        print("User added successfully.")
        self.log_operation(f"Added new user with ID: {user_id}")

    def list_users(self):
        if self.users:
            print("\n===== List of Users =====")
            for user in self.users:
                print(user)
        else:
            print("No users available.")

    def search_user(self, keyword):
        found = False
        for user in self.users:
            if keyword.lower() in user.name.lower() or keyword.lower() in user.user_id.lower():
                print(user)
                found = True
        if not found:
            print("User not found.")

    def delete_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]
        print("User deleted successfully.")
        self.log_operation(f"Deleted user with ID: {user_id}")

    def check_out_book(self, isbn, user_id):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print("Book checked out successfully.")
                    self.log_operation(f"Checked out book with ISBN: {isbn} by user ID: {user_id}")
                else:
                    print("Book is already checked out.")
                break
        else:
            print("Book not found.")

    def check_in_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    print("Book checked in successfully.")
                    self.log_operation(f"Checked in book with ISBN: {isbn}")
                else:
                    print("Book is already checked in.")
                break
        else:
            print("Book not found.")

    def log_operation(self, operation):
        with open("log.txt", "a") as logfile:
            logfile.write(operation + "\n")
