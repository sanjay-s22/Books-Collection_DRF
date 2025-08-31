from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'), # List/create books
    path('books/<int:book_id>/', views.book_detail, name='book-detail'), # Get/update/delete specific book
]