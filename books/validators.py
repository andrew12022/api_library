from datetime import datetime

from django.core.exceptions import ValidationError


def validate_year_of_publication(value):
    """Валидация для года публикации."""
    current_year = datetime.now().year
    min_year = 1900
    if value > current_year:
        raise ValidationError(
            'Ошибка! '
            f'Год публикации {value} не может быть больше {current_year}'
        )
    elif value < min_year:
        raise ValidationError(
            'Ошибка! '
            f'Год публикации {value} не может быть меньше {min_year}'
        )
