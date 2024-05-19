from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path(
        '',
        views.index,
        name='index',
    ),
    path(
        'books/<int:id>/',
        views.books_detail,
        name='books_detail',
    ),
    path(
        'author/<slug:author_slug>/',
        views.author_books,
        name='author_books',
    ),
    path(
        'genre/<slug:genre_slug>/',
        views.genre_books,
        name='genre_books',
    ),
    path(
        'seires/<slug:series_slug>/',
        views.series_books,
        name='series_books',
    ),
    path(
        'publisher/<slug:publisher_slug>/',
        views.publisher_books,
        name='publisher_books',
    ),
    path(
        'books/<int:pk>/review/',
        views.ReviewCreateView.as_view(),
        name='add_review',
    ),
    path(
        'books/<int:book_id>/edit_review/<int:pk>/',
        views.ReviewUpdateView.as_view(),
        name='edit_review',
    ),
    path(
        'books/<int:book_id>/delete_review/<int:pk>/',
        views.ReviewDeleteView.as_view(),
        name='delete_review',
    ),
]
