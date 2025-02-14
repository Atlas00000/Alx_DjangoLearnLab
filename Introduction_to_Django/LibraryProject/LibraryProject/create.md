# Create Operation

## **Objective**
This operation demonstrates how to create a new Book instance in Django using the ORM.

## **Command Used**
```python
from bookshelf.models import Book

# Creating a Book instance
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Display the created book
print(book1)
