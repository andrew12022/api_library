import csv
import os

from django.core.management.base import BaseCommand, CommandError

from api_library.settings import BASE_DIR
from books.models import Author, Book, Genre, Publisher, Series

FILE_PATH = os.path.join(
    BASE_DIR,
    'data'
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:

            with open(
                os.path.join(FILE_PATH, 'author.csv')
            ) as file_csv:
                data = csv.DictReader(file_csv, delimiter=',')
                for row in data:
                    Author.objects.create(
                        name=row['name'],
                        slug=row['slug'],
                    )
                print('Файл author.csv успешно импортировал данные в БД')

            with open(
                os.path.join(FILE_PATH, 'genre.csv')
            ) as file_csv:
                data = csv.DictReader(file_csv, delimiter=',')
                for row in data:
                    Genre.objects.create(
                        name=row['name'],
                        slug=row['slug'],
                    )
                print('Файл genre.csv успешно импортировал данные в БД')

            with open(
                os.path.join(FILE_PATH, 'series.csv')
            ) as file_csv:
                data = csv.DictReader(file_csv, delimiter=',')
                for row in data:
                    Series.objects.create(
                        name=row['name'],
                        slug=row['slug'],
                    )
                print('Файл series.csv успешно импортировал данные в БД')

            with open(
                os.path.join(FILE_PATH, 'publisher.csv')
            ) as file_csv:
                data = csv.DictReader(file_csv, delimiter=',')
                for row in data:
                    Publisher.objects.create(
                        name=row['name'],
                        slug=row['slug'],
                    )
                print('Файл publisher.csv успешно импортировал данные в БД')

            with open(
                os.path.join(FILE_PATH, 'book.csv')
            ) as file_csv:
                data = csv.DictReader(file_csv, delimiter=',')
                for row in data:
                    Book.objects.create(
                        name=row['name'],
                        slug=row['slug'],
                        description=row['description'],
                        author_id=row['author_id'],
                        genre_id=row['genre_id'],
                        series_id=row['series_id'],
                        publisher_id=row['publisher_id'],
                        year_of_publication=row['year_of_publication'],
                        page_count=row['page_count'],
                        isbn=row['isbn'],
                    )
                print('Файл book.csv успешно импортировал данные в БД')

        except Exception as error:
            raise CommandError(f'Произошла ошибка: {error}')

        self.stdout.write(
            self.style.SUCCESS(
                ('Данные были загружены в БД')
            )
        )
