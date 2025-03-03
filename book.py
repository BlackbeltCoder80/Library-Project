class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.is_borrowed = False  # Track if the book is borrowed

    def borrow_book(self):
        """Marks the book as borrowed if it's available."""
        if not self.is_borrowed:
            self.is_borrowed = True
            return f'You have borrowed "{self.title}".'
        return f'Sorry, "{self.title}" is already borrowed.'

    def return_book(self):
        """Marks the book as available if it was borrowed."""
        if self.is_borrowed:
            self.is_borrowed = False
            return f'You have returned "{self.title}".'
        return f'"{self.title}" was not borrowed.'

    def __str__(self):
        """String representation of the book."""
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f'"{self.title}" by {self.author} | Genre: {self.genre} | Published: {self.publication_date} | Status: {status}'
