class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow_book()
            self.borrowed_books.append(book.title)
            return f'{self.name} borrowed "{book.title}".'
        return f'"{book.title}" is not available.'

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)
            return f'{self.name} returned "{book.title}".'
        return f'{self.name} does not have "{book.title}".'

    def __str__(self):
        borrowed = ", ".join(self.borrowed_books) if self.borrowed_books else "No books borrowed"
        return f'User: {self.name} | ID: {self.user_id} | Borrowed Books: {borrowed}'