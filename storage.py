import json

class DataManager:
    def __init__(self, filename):
        self.filename = filename
    
    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_data(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

class BookManager(DataManager):
    def __init__(self, filename):
        super().__init__(filename)
    
    def load_books(self):
        return self.load_data()
    
    def save_books(self, books):
        self.save_data(books)

class UserManager(DataManager):
    def __init__(self, filename):
        super().__init__(filename)
    
    def load_users(self):
        return self.load_data()
    
    def save_users(self, users):
        self.save_data(users)

if __name__ == "__main__":
    # Example usage
    book_file = input("Enter the path for the books JSON file: ")
    book_manager = BookManager(book_file)
    books = book_manager.load_books()
    print("Loaded books:", books)
    
    # Modify books if needed
    
    book_manager.save_books(books)

    user_file = input("Enter the path for the users JSON file: ")
    user_manager = UserManager(user_file)
    users = user_manager.load_users()
    print("Loaded users:", users)
    
    # Modify users if needed
    
    user_manager.save_users(users)
