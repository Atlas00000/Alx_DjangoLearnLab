import os
import django

# Set up Django environment (Ensure "LibraryProject" is your actual project name)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

# Import models
from relationship_app.models import Author, Book, Library, Librarian

# Query: Get all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        return [book.title for book in author.books.all()]
    return []

# Query: List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return [book.title for book in library.books.all()]
    return []

# Query: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library and hasattr(library, 'librarian'):
        return library.librarian.name
    return "No librarian assigned"

# Example Usage
if __name__ == "__main__":
    print("Books by J.K. Rowling:", get_books_by_author("J.K. Rowling"))
    print("Books in Central Library:", get_books_in_library("Central Library"))
    print("Librarian of Central Library:", get_librarian_for_library("Central Library"))
