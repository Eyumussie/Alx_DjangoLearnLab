
**`retrieve.md`:**

```markdown
### Retrieve Operation

**Command:**

```python
# Retrieve all books
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)

# Retrieve a specific book
book = Book.objects.get(title="1984")
print("Retrieved:", book.title, book.author, book.publication_year)
