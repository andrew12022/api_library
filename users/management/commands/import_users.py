import csv
import os

from django.core.management.base import BaseCommand, CommandError

from api_library.settings import BASE_DIR
from users.models import User

FILE_PATH = os.path.join(
    BASE_DIR,
    'data'
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:

            with open(
                os.path.join(FILE_PATH, 'user.csv')
            ) as file_csv:
                data = csv.DictReader(file_csv, delimiter=',')
                for row in data:
                    User.objects.create(
                        email=row['email'],
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        middle_name=row['middle_name'],
                        username=row['username'],
                        gender=row['gender'],
                        date_of_birthday=row['date_of_birthday'],
                    )
                print('Файл user.csv успешно импортировал данные в БД')

        except Exception as error:
            raise CommandError(f'Произошла ошибка: {error}')

        self.stdout.write(
            self.style.SUCCESS(
                ('Данные были загружены в БД')
            )
        )
