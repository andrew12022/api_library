# Generated by Django 4.1.13 on 2024-04-30 15:51

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import books.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'объект "Автор"',
                'verbose_name_plural': 'Автора',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'объект "Жанр"',
                'verbose_name_plural': 'Жанры',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'объект "Издательство"',
                'verbose_name_plural': 'Издательства',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'объект "Серия"',
                'verbose_name_plural': 'Серии',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Идентификатор')),
                ('description', models.TextField(blank=True, help_text='Поле может быть пустым', null=True, verbose_name='Описание')),
                ('year_of_publication', models.PositiveSmallIntegerField(validators=[books.validators.validate_year_of_publication], verbose_name='Год издания')),
                ('page_count', models.PositiveSmallIntegerField(help_text='Укажите количество страниц от 1 до 5000', validators=[django.core.validators.MinValueValidator(1, 'Ошибка! Минимальное значение = 1'), django.core.validators.MaxValueValidator(5000, 'Ошибка! Максимальное значение = 5000')], verbose_name='Количество страниц')),
                ('isbn', models.CharField(help_text='Введите ISBN в формате: 978-5-93673-265-2', max_length=17, validators=[django.core.validators.RegexValidator(message='Ошибка! Проверьте вводимый формат', regex='^\\d{3}-\\d{1}-\\d{5}-\\d{3}-\\d{1}$')], verbose_name='ISBN')),
                ('availability', models.BooleanField(verbose_name='Наличие')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='books.author', verbose_name='Автор')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_genre', to='books.genre', verbose_name='Жанр')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_publisher', to='books.publisher', verbose_name='Издательство')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_series', to='books.series', verbose_name='Серия')),
            ],
            options={
                'verbose_name': 'объект "Книга"',
                'verbose_name_plural': 'Книги',
                'ordering': ['-id'],
            },
        ),
    ]
