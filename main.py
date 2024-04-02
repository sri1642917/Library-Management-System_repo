from library import Library

def main():
    library = Library()
    while True:
        print("\n===== Library Management System =====")
        print("1. Manage Books")
        print("2. Manage Users")
        print("3. Check Out a Book")
        print("4. Check In a Book")
        print("5. List All Books")
        print("6. Search for a Book")
        print("7. List All Users")
        print("8. Search for a User")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manage_books(library)

        elif choice == '2':
            manage_users(library)

        elif choice == '3':
            isbn = input("Enter the ISBN of the book to check out: ")
            user_id = input("Enter the user ID: ")
            library.check_out_book(isbn, user_id)

        elif choice == '4':
            isbn = input("Enter the ISBN of the book to check in: ")
            library.check_in_book(isbn)

        elif choice == '5':
            library.list_books()

        elif choice == '6':
            keyword = input("Enter the title, author, or ISBN to search for: ")
            library.search_book(keyword)

        elif choice == '7':
            library.list_users()

        elif choice == '8':
            keyword = input("Enter the name or user ID to search for: ")
            library.search_user(keyword)

        elif choice == '9':
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

def manage_books(library):
    while True:
        print("\n===== Manage Books =====")
        print("1. Add a Book")
        print("2. Delete a Book")
        print("3. Update Book Availability")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            library.add_book(title, author, isbn)

        elif choice == '2':
            isbn = input("Enter the ISBN of the book to delete: ")
            library.delete_book(isbn)

        elif choice == '3':
            isbn = input("Enter the ISBN of the book to update availability: ")
            availability = input("Enter availability (True/False): ")
            library.update_book_availability(isbn, availability)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def manage_users(library):
    while True:
        print("\n===== Manage Users =====")
        print("1. Add a User")
        print("2. Delete a User")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the user: ")
            user_id = input("Enter the user ID: ")
            library.add_user(name, user_id)

        elif choice == '2':
            user_id = input("Enter the user ID to delete: ")
            library.delete_user(user_id)

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
