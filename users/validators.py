from datetime import date

from django.core.exceptions import ValidationError


def validate_username(value):
    if value.lower() == 'me':
        raise ValidationError(
            'Ошибка! Использовать "me" в качестве `username` запрещено'
        )


def validate_date_of_birthday(value):
    min_age = 14
    td = date.today()
    if value > td:
        raise ValidationError(
            f'Ошибка! Дата рождения {value} не может быть позже чем {td}'
        )
    elif (
        td.year - value.year - ((td.month, td.day) < (value.month, value.day))
    ) < min_age:
        raise ValidationError(
            f'Ошибка! Минимальный возраст регистрации = {min_age} лет'
        )
