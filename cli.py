from library import Library
from book_data_handler import save_data, load_data

def main():
    library = Library()
    load_data(library)  # Load existing data

    # Adding sample data (Wheel of Time & Mistborn Series)
    library.add_author("Robert Jordan", "Author of Wheel of Time")
    library.add_author("Brandon Sanderson", "Finished WoT, Mistborn series author")
    library.add_book("The Eye of the World", "Robert Jordan", "Fantasy", "1990")
    library.add_book("The Final Empire", "Brandon Sanderson", "Fantasy", "2006")

    while True:
        print("\nWelcome to the Library Management System!")
        print("1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n1. Add a new book\n2. Search for a book\n3. Display all books\n4. Borrow a book\n5. Return a book")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                genre = input("Enter book genre: ")
                pub_date = input("Enter publication date: ")
                print(library.add_book(title, author, genre, pub_date))

            elif sub_choice == "2":
                title = input("Enter book title to search: ")
                book = library.find_book(title)
                print(book if book else "Book not found.")

            elif sub_choice == "3":
                print("\nBooks in Library:")
                print(library.display_books())

            elif sub_choice == "4":  # Borrow a book
                title = input("Enter book title to borrow: ")
                borrower_name = input("Enter your name: ")
                print(library.borrow_book(title, borrower_name))

            elif sub_choice == "5":  # Return a book
                title = input("Enter book title to return: ")
                borrower_name = input("Enter your name: ")
                print(library.return_book(title, borrower_name))

        elif choice == "2":
            print("\n1. Add a new user\n2. View user details\n3. Display all users")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                print(library.add_user(name, user_id))
            elif sub_choice == "2":
                name = input("Enter user name to view details: ")
                user = library.find_user(name)
                print(user if user else "User not found.")
            elif sub_choice == "3":
                print("\nRegistered Users:")
                print(library.display_users())

        elif choice == "3":
            print("\n1. Display all authors")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                print("\nAuthors:")
                print(library.display_authors())

        elif choice == "4":
            print("Saving data before quitting...")
            save_data(library)
            print("Data saved. Exiting program.")
            print("Goodbye!")
        break
    

if __name__ == "__main__":
    main()
