class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """Allows the user to borrow a book if it's available."""
        if not book.is_borrowed:
            book.borrow_book(self.name)  # Pass borrower's name
            self.borrowed_books.append(book.title)
            return f'{self.name} borrowed "{book.title}".'
        return f'Sorry, "{book.title}" is already borrowed by {book.borrowed_by}.'

    def return_book(self, book):
        """Allows the user to return a book they borrowed."""
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)
            return f'{self.name} returned "{book.title}".'
        return f'{self.name} does not have "{book.title}".'

    def __str__(self):
        borrowed = ", ".join(self.borrowed_books) if self.borrowed_books else "No books borrowed"
        return f'User: {self.name} | ID: {self.user_id} | Borrowed Books: {borrowed}'
  




