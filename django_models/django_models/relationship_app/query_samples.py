import os
import django

# Ensure Django settings are loaded
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')  # ✅ Fixed project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Query all books written by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")
        return []

def get_books_in_library(library_name):
    """List all books available in a library."""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
        return []

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a given library."""
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to the library '{library_name}'.")
    return None

if __name__ == "__main__":
    # Sample usage
    sample_author = "John Doe"
    sample_library = "Central Library"

    print(f"Books by '{sample_author}':")
    books = get_books_by_author(sample_author)
    for book in books:
        print(f"- {book.title}")

    print(f"\nBooks in '{sample_library}':")
    books = get_books_in_library(sample_library)
    for book in books:
        print(f"- {book.title}")

    print(f"\nLibrarian for '{sample_library}':")
    librarian = get_librarian_for_library(sample_library)
    if librarian:
        print(librarian.name)
