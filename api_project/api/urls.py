from django.urls import path
from .views import BookListCreate, BookDetail

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),  # List all books or create a new book
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),  # Retrieve, update, or delete a book by ID
]
