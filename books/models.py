from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from api_library import constants
from books.validators import validate_year_of_publication
from users.models import User


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
        related_name='books',
        verbose_name='Автор',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Жанр',
    )
    series = models.ForeignKey(
        Series,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Серия',
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='books',
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
                    'Ошибка! Минимальное значение = '
                    f'{constants.MIN_VALIDATION_VALUE_OF_PAGE_COUNT}'
                ),
            ),
            MaxValueValidator(
                constants.MAX_VALIDATION_VALUE_OF_PAGE_COUNT,
                (
                    'Ошибка! Максимальное значение = '
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

    class Meta:
        ordering = ['-id']
        verbose_name = 'объект "Книга"'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(
        verbose_name='Текст отзыва',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(
                constants.MIN_VALIDATION_VALUE_OF_RATING,
                (
                    'Ошибка! Минимальное значение = '
                    f'{constants.MIN_VALIDATION_VALUE_OF_RATING}'
                ),
            ),
            MaxValueValidator(
                constants.MAX_VALIDATION_VALUE_OF_RATING,
                (
                    'Ошибка! Максимальное значение = '
                    f'{constants.MAX_VALIDATION_VALUE_OF_RATING}'
                ),
            ),
        ],
        verbose_name='Рейтинг',
        help_text='Укажите рейтинг книги от 1 до 10',
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Книга',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва',
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'объект "Отзыв"'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'book'],
                name='unique_author_book',
            )
        ]

    def __str__(self):
        return self.text


class Favourites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favourites',
        verbose_name='Пользователь',
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='favourites',
        verbose_name='Книга',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'объект "Избранное"'
        verbose_name_plural = 'Избранное'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'book'],
                name='unique_user_book',
            )
        ]

    def __str__(self):
        return (
            f'{self.user} добавил рецепт "{self.book}" в Избранное'
        )
