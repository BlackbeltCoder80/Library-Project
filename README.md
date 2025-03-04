# Library Managment Systems-Project

This book managment system will allow you to manage all your library books in your personal online library. 
So when you let friends use your book you can track who had it last and how long they have had it for.

# Overview
The Library mangement system is a simple and efficient way to manage books, users, and authors in a personal library. 
This is command line application allows users to add borrow, returnmm and search for books autiomantically saving all data for future user.

# Features
- Manage Books
- Track Borrowed Books
- User Management
- Author Management 
- Auto Saving

# Installation Guide
Option 1: Running it with Python (Developer Use)
1. Install Python (if not already installed):
2. Install Required Packages (pip install tabulate)
3. Download the repository as a zip and extrat it
 a. Clone it using Git: git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME (you tube can explain more).
4. Run Program (python cli.py or py cli.py)

# Option 2: Running as app in Windows Only
1. download cli.exe
2. double-click cli.exe (launch the library system)
3. If you get a windos security warning: I got security warning just "Run Anyway".



Welcome to the Library Home Management System


How to use the system:
# Display Current Books
1. Run the program Library Management System
 a. this will take you to Book Operation
 b. Display Books by pressing #1

# Add New Book
2. Press 1 Book Operations
 a. press #1 to " Add a new book.
 b. Follow on screen instructions.
 # Enter:
  a. Title
  b. Author
  c. Genre
  d. Publication Year
  
# Borrow a Book
3.  Press 1 Book Operations
 a. Select Book Operations 1
 b. Select Borrow a book 4
 c. Enter the Book Title and User Name.
 
 # Retun Boook
 4. 
  a. Select Book Operations (1).
  b. Select Return a book (5).
  c. Enter the Book Title and User Name.

# Viewing Books
5. 
a. To see books 1, 3
b. To see all users 2, 3
c. To view user details 2, 2

# Storage
All books, usersm and authors are saved in library_data.json.
When you quit the data should save automatically.
All previous data will load when program is opened.

# Future Improvements

If you are a developer looking to contribute, here are potential improvements:

# Graphical User Interface (GUI): 
Upgrade from CLI to a UI using Tkinter or PyQt. ( I dont hav emusch knowledge here but when I do I will update as I learn)

# Book Reservations: 
Allow users to reserve books that are currently unavailable.

# Fine System: 
Implement overdue book tracking and fine calculations.

# Export Data: 
Allow users to export data to CSV or PDF for easier tracking.

If you're interested in contributing, feel free to fork the repository and submit a pull request.

Need Help?

If you run into any issues or have questions, please contact me at:📧 blackbeltcoder80@gmail.com

🔥 Enjoy using the Library Management System! 🚀

That was a lot tired...



# Developer Note 
1. Use this code to update exe files in code (py -m PyInstaller --onefile cli.py) Do this first Delete: dist folder, pycahe, and buiuld before.





