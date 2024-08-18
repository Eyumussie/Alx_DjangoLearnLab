# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView
from .views import CustomLoginView, CustomLogoutView, register, list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', CustomLoginView.as_view(login.html), name='login'),
    path('logout/', CustomLogoutView.as_view(logout.html), name='logout'),
    path('register/', register, name='register'),
    path('books/', list_books, name='list-books'),  # Existing URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # Existing URL
]

