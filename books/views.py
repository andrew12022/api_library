from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from books.models import Author, Book, Genre, Publisher, Series


def index(request):
    book_list = Book.objects.select_related(
        'author',
        'genre',
        'series',
        'publisher',
    )
    paginator = Paginator(book_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'books/index.html', context)


def books_detail(request, id):
    book = get_object_or_404(
        Book.objects.select_related(
            'author',
            'genre',
            'series',
            'publisher',
        ), id=id
    )
    context = {
        'book': book,
    }
    return render(request, 'books/detail.html', context)


def author_books(request, author_slug):
    author = get_object_or_404(
        Author.objects.filter(
            slug=author_slug,
        )
    )
    book_list = author.books.all()
    paginator = Paginator(book_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'author': author,
    }
    return render(request, 'books/author.html', context)


def genre_books(request, genre_slug):
    genre = get_object_or_404(
        Genre.objects.filter(
            slug=genre_slug,
        )
    )
    book_list = genre.books.all()
    paginator = Paginator(book_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'genre': genre,
    }
    return render(request, 'books/genre.html', context)


def series_books(request, series_slug):
    series = get_object_or_404(
        Series.objects.filter(
            slug=series_slug,
        )
    )
    book_list = series.books.all()
    paginator = Paginator(book_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'series': series,
    }
    return render(request, 'books/series.html', context)


def publisher_books(request, publisher_slug):
    publisher = get_object_or_404(
        Publisher.objects.filter(
            slug=publisher_slug,
        )
    )
    book_list = publisher.books.all()
    paginator = Paginator(book_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'publisher': publisher,
    }
    return render(request, 'books/publisher.html', context)
