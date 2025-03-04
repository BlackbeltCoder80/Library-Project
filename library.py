from book import Book
from user import User
from author import Author
from tabulate import tabulate

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def add_book(self, title, author, genre, publication_date):
        book = Book(title, author, genre, publication_date)
        self.books.append(book) #  Prints when book is added # (if you can fix this please help, Ive tried several times...:(
        return f'Book "{title}" added successfully.'

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)
        return f'User "{name}" added successfully.'

    def add_author(self, name, biography):
        author = Author(name, biography)
        self.authors.append(author)
        return f'Author "{name}" added successfully.'

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        if not self.books:
            return "No books available."
        headers = ["Title", "Author", "Genre", "Published", "Status"]
        table = [[book.title, book.author, book.genre, book.publication_date, "Borrowed" if book.is_borrowed else "Available"] for book in self.books]
        return tabulate(table, headers, tablefmt="fancy_grid")

    def display_users(self):
        if not self.users:
            return "No users registered."
        headers = ["Name", "User ID", "Borrowed Books"]
        table = [[user.name, user.user_id, ", ".join(user.borrowed_books) if user.borrowed_books else "None"] for user in self.users]
        return tabulate(table, headers, tablefmt="fancy_grid")

    def display_authors(self):
        if not self.authors:
            return "No authors found."
        headers = ["Name", "Biography"]
        table = [[author.name, author.biography] for author in self.authors]
        return tabulate(table, headers, tablefmt="fancy_grid")
    
    def find_user(self, name):
        """Finds User by Name"""
        for user in self.users:
            if user.name.lower() == name.lower():
                return user
        return None
    def borrow_book(self, title, borrower_name):
        """Allows a registered user to borrow a book"""
        book = self.find_book(title)
        user = self.find_user(borrower_name)
        if not user:
            return f"Error: '{borrower_name}' is not a registered user. Please add user first"
        if book:
            return user.borrow_book(book) #borrow book from user class
        return "Book not found"
        