from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from api_library import constants
from users.validators import validate_date_of_birthday, validate_username


class User(AbstractUser):
    GENDER_CHOICES = [
        ('мужской', 'Мужской'),
        ('женский', 'Женский'),
    ]
    email = models.EmailField(
        max_length=constants.MAX_LENGTH_FIELDS_OF_EMAIL,
        unique=True,
        verbose_name='Электронная почта',
        help_text=(
            'Указанная почта будет использоваться '
            'в качестве логина для входа в учётную запись'
        ),
    )
    last_name = models.CharField(
        max_length=constants.MAX_LENGTH_FIELDS_OF_NAME,
        verbose_name='Фамилия',
    )
    first_name = models.CharField(
        max_length=constants.MAX_LENGTH_FIELDS_OF_NAME,
        verbose_name='Имя',
    )
    middle_name = models.CharField(
        null=True,
        blank=True,
        max_length=constants.MAX_LENGTH_FIELDS_OF_NAME,
        verbose_name='Отчество',
        help_text='Если у вас нет отчества, оставляйте поле пустым',
    )
    username = models.CharField(
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message='Ошибка! Проверьте вводимый формат'
            ),
            validate_username,
        ],
        max_length=constants.MAX_LENGTH_FIELDS_OF_USERNAME,
        unique=True,
        verbose_name='Уникальный ник пользователя',
    )
    gender = models.CharField(
        null=True,
        blank=True,
        max_length=constants.MAX_LENGTH_FIELDS_OF_GENDER,
        choices=GENDER_CHOICES,
        verbose_name='Пол',
    )
    date_of_birthday = models.DateField(
        validators=[validate_date_of_birthday],
        null=True,
        blank=True,
        verbose_name='Дата рождения',
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'middle_name',
        'gender',
        'date_of_birthday',
    )

    @property
    def age(self):
        if self.date_of_birthday:
            td = date.today()
            db = self.date_of_birthday
            age = td.year - db.year - ((td.month, td.day) < (db.month, db.day))
            return age
        else:
            return None

    class Meta:
        ordering = ['-id']
        verbose_name = 'объект "Пользователь"'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
