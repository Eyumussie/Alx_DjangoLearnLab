from django.urls import path
from . import views 
from .views import list_books
from django.contrib.auth import views as auth_views
from . import views

 
urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # This is the line you need
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),  # Updated path for adding a book
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # Updated path for editing a book
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),  # Updated path for deleting a book
]
