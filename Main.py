Class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def search_by_title(self, title):
        found_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                found_books.append(book)
        return found_books

    def search_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                found_books.append(book)
        return found_books

    def display_books(self):
        if len(self.books) == 0:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}")

# Create a library object
library = Library()

# Function to add books to the library
def add_books():
    while True:
        title = input("Enter the book title (or 'q' to quit): ")
        if title.lower() == 'q':
            break
        author = input("Enter the author of book: ")
        library.add_book(title, author)

# Function to search books by title
def search_books_by_title():
    title = input("Enter the book title to search for: ")
    found_books = library.search_by_title(title)
    if len(found_books) == 0:
        print("No books found with that title.")
    else:
        print(f"Found {len(found_books)} book(s) with the title '{title}':")
        for book in found_books:
            print(f"Title: {book.title}, Author: {book.author}")

# Function to search books by author
def search_books_by_author():
    author = input("Enter the book author to search for: ")
    found_books = library.search_by_author(author)
    if len(found_books) == 0:
        print("No books found by that author.")
    else:
        print(f"Found {len(found_books)} book(s) by the author '{author}':")
        for book in found_books:
            print(f"Title: {book.title}, Author: {book.author}")

# Function to display all books in the library
def display_all_books():
    library.display_books()

# Main menu
while True:
    print("\nDigital Library")
    print("1. Add books")
    print("2. Search books by title")
    print("3. Search books by author")
    print("4. Display all books")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_books()
    elif choice == '2':
        search_books_by_title()
    elif choice == '3':
        search_books_by_author()
    elif choice == '4':
        display_all_books()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
