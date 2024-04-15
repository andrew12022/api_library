from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from api_library import constants
from books.validators import validate_year_of_publication


class NameAndSlugModel(models.Model):
    """Абстрактная модель для всех моделей."""
    name = models.CharField(
        max_length=constants.MAX_LENGTH_FIELDS_OF_NAME_AND_SLUG,
        verbose_name='Название',
    )
    slug = models.SlugField(
        max_length=constants.MAX_LENGTH_FIELDS_OF_NAME_AND_SLUG,
        unique=True,
        verbose_name='Идентификатор',
    )

    class Meta:
        abstract = True


class Author(NameAndSlugModel):
    """Модель для автора."""
    class Meta:
        ordering = ['-id']
        verbose_name = 'объект "Автор"'
        verbose_name_plural = 'Автора'

    def __str__(self):
        return self.name


class Genre(NameAndSlugModel):
    """Модель для жанра."""
    class Meta:
        ordering = ['-id']
        verbose_name = 'объект "Жанр"'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Series(NameAndSlugModel):
    """Модель для серии."""
    class Meta:
        ordering = ['-id']
        verbose_name = 'объект "Серия"'
        verbose_name_plural = 'Серии'

    def __str__(self):
        return self.name


class Publisher(NameAndSlugModel):
    """Модель для издательства."""
    class Meta:
        ordering = ['-id']
        verbose_name = 'объект "Издательство"'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return self.name


class Book(NameAndSlugModel):
    """Модель для книги."""
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',
        help_text='Поле может быть пустым',
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='book_author',
        verbose_name='Автор',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='book_genre',
        verbose_name='Жанр',
    )
    series = models.ForeignKey(
        Series,
        on_delete=models.CASCADE,
        related_name='book_series',
        verbose_name='Серия',
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='book_publisher',
        verbose_name='Издательство',
    )
    year_of_publication = models.PositiveSmallIntegerField(
        validators=[validate_year_of_publication],
        verbose_name='Год издания',
    )
    page_count = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(
                constants.MIN_VALIDATION_VALUE_OF_PAGE_COUNT,
                (
                    'Минимальное значение = '
                    f'{constants.MIN_VALIDATION_VALUE_OF_PAGE_COUNT}'
                ),
            ),
            MaxValueValidator(
                constants.MAX_VALIDATION_VALUE_OF_PAGE_COUNT,
                (
                    'Максимальное значение = '
                    f'{constants.MAX_VALIDATION_VALUE_OF_PAGE_COUNT}'
                ),
            ),
        ],
        verbose_name='Количество страниц',
        help_text='Укажите количество страниц от 1 до 5000',
    )
    isbn = models.CharField(
        validators=[
            RegexValidator(
                regex=r'^\d{3}-\d{1}-\d{5}-\d{3}-\d{1}$',
                message='Ошибка! Проверьте вводимый формат',
            )
        ],
        max_length=constants.MAX_LENGTH_FIELDS_OF_ISBN,
        verbose_name='ISBN',
        help_text='Введите ISBN в формате: 978-5-93673-265-2',
    )
    availability = models.BooleanField(
        verbose_name='Наличие',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'объект "Книга"'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name
