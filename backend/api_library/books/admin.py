from django.contrib import admin

from books.models import Author, Book, Genre, Publisher, Series


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'description',
        'author',
        'genre',
        'series',
        'publisher',
        'year_of_publication',
        'page_count',
        'isbn',
        'availability',
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}
