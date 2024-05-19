from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from rest_framework.authtoken.models import TokenProxy

from users.models import User

admin.site.empty_value_display = 'Не задано'


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'gender',
        'date_of_birthday',
        'is_superuser',
        'is_staff',
    )
    search_fields = (
        'username',
    )
    list_filter = (
        'gender',
        'is_superuser',
        'is_staff',
    )


UserAdmin.fieldsets += (
    (
        'Дополнительные поля',
        {
            'fields': (
                'middle_name',
                'gender',
                'date_of_birthday',
            ),
        }
    ),
)

admin.site.unregister(Group)
admin.site.unregister(TokenProxy)
