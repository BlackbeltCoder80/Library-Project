import json
import os
from datetime import datetime
from book import Book

DATA_FILE = "library_data.json"  #  Updates File Name 

def save_data(library):
    """Saves books, users, and authors to a JSON file."""
    data = {
        "books": [
            {
                "title": book.title,
                "author": book.author,
                "genre": book.genre,
                "publication_date": book.publication_date,
                "is_borrowed": book.is_borrowed,
                "borrowed_by": book.borrowed_by if book.borrowed_by else None,
                "borrowed_date": book.borrowed_date.strftime("%Y-%m-%d %H:%M:%S") if book.is_borrowed_date else None
            }
            for book in library.books
        ],
        "users": [
            {"name": user.name, "user_id": user.user_id, "borrowed_books": user.borrowed_books}
            for user in library.users
        ],
        "authors": [
            {"name": author.name, "biography": author.biography}
            for author in library.authors
        ]
    }
    print("Saving data to library_data.json...")  #  confirmation
    with open("library_data.json", "w") as file:
        json.dump(data, file, indent=4)
    print(" Data saved successfully!")  # success message
    print(f"Books being saved: {len(library.books)}") 

def load_data(library):
    """Loads the library data from a file."""
    if not os.path.exists(DATA_FILE):
        save_data(library)  
        return  # No data to load yet

    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Error: Could not load data. The JSON file may be corrupted.")
            return

    for book_data in data.get("books", []):
        book = Book(
            book_data["title"],
            book_data["author"],
            book_data["genre"],
            book_data["publication_date"]
        )
        book.is_borrowed = book_data["is_borrowed"]
        book.borrowed_by = book_data.get("borrowed_by", None)  
        book.borrowed_date = (
            datetime.strptime(book_data["borrowed_date"], "%Y-%m-%d %H:%M:%S") 
            if book_data.get("borrowed_date") 
            else None
        )
        library.books.append(book)
