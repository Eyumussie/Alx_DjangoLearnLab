
**`update.md`:**

```markdown
### Update Operation

**Command:**

```python
# Update the book's title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
updated_book = Book.objects.get(id=book.id)
print("Updated:", updated_book.title)
