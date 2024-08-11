
**`delete.md`:**

```markdown
### Delete Operation

**Command:**

```python
# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print("Books after deletion:", list(books))
