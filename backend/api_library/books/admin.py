from django.contrib import admin

from books.models import Author, Book, Genre, Publisher, Series

admin.site.empty_value_display = 'Не задано'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Админ модель для автора."""
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Админ модель для жанра."""
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    """Админ модель для серии."""
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    """Админ модель для издательства."""
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Админ модель для книги."""
    list_display = (
        'name',
        'author',
        'genre',
        'series',
        'publisher',
        'year_of_publication',
        'page_count',
        'availability',
    )
    list_editable = (
        'availability',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'author',
        'genre',
        'series',
        'publisher',
        'availability',
    )
    raw_id_fields = (
        'author',
        'genre',
        'series',
        'publisher',
    )
    prepopulated_fields = {'slug': ('name',)}
