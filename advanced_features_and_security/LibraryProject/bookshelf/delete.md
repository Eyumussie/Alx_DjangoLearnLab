### Delete Operation

**Command:**

```python
from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print("Books after deletion:", list(books))
