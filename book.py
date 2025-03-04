from datetime import datetime

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.is_borrowed = False
        self.is_borrowed_date = None  # Track if the book is borrowed or not
        self.borrowed_by = None # Track who borrowed your book

    def borrow_book(self, borrower_name):
        """Marks the book as borrowed,records the date, and tracks the borrower
        ."""
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_date = datetime.now()
            self.borrowed_by = borrower_name
            return f'{borrower_name} has borrowed "{self.title}".'
        return f'Sorry, "{self.title}" is already borrowed by {self.borrowed_by}.'

    def return_book(self):
        """Marks the book as available and clears borrower details."""
        if self.is_borrowed:
            days_checked_out = self.get_borrow_duration()
            borrower = self.borrowed_by
            self.is_borrowed = False
            self.borrowed_date = None
            self.borrowed_by = None
            return f'"{self.title}" was returned by {borrower}. It was checked out for {days_checked_out} days.'
        return f'"{self.title}" was not borrowed.'

    def get_borrow_duration(self):
        """Calculates how long the book has been borrowed in days."""
        if self.is_borrowed and self.borrowed_date:
            duration = datetime.now() - self.borrowed_date
            return duration.days
        return 0  # If not borrowed, return 0 days

    def __str__(self):
        """String representation of the book."""
        status = "Available" if not self.is_borrowed else f"Borrowed by {self.borrowed_by} ({self.get_borrow_duration()} days)"
        return f'"{self.title}" by {self.author} | Genre: {self.genre} | Published: {self.publication_date} | Status: {status}'
